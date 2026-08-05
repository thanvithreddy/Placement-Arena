import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Document, DocumentChunk, TextbookChunk, StudentBKTTracker, TelemetryLog
from .serializers import TextbookChunkSerializer, StudentBKTTrackerSerializer
from .rag_engine import get_text_embedding, generate_socratic_guidance

logger = logging.getLogger('placement_arena')


def _is_admin(user):
    """Check if user has admin privileges."""
    return user.is_staff or (hasattr(user, 'role') and user.role == 'admin')


class IngestTextbookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not _is_admin(request.user):
            return Response({'error': 'Admin access required'}, status=403)

        subject = request.data.get('subject', 'verbal')
        topic_slug = request.data.get('topic_slug', 'general')
        chapter_title = request.data.get('chapter_title', 'Master Notes')
        content = request.data.get('content', '')

        if not content:
            return Response({'error': 'Content is required'}, status=400)

        # Split content into ~300 character chunks with 50 character overlap
        chunk_size = 300
        overlap = 50
        chunks = []
        start = 0
        idx = 0

        while start < len(content):
            end = min(start + chunk_size, len(content))
            chunk_text = content[start:end]
            vec = get_text_embedding(chunk_text)

            chunk_obj = TextbookChunk.objects.create(
                subject=subject,
                topic_slug=topic_slug,
                chapter_title=chapter_title,
                chunk_index=idx,
                content=chunk_text,
                vector_json=vec
            )
            chunks.append(chunk_obj)
            idx += 1
            start += (chunk_size - overlap)

        return Response({
            'message': f'Successfully ingested {len(chunks)} textbook chunks for {subject}/{topic_slug}!',
            'chunk_count': len(chunks)
        })

class TrueAIRAGAskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        query = request.data.get('query', '')
        subject = request.data.get('subject', 'verbal')
        topic_slug = request.data.get('topic_slug', '')
        cognitive_state = request.data.get('cognitive_state', 'OPTIMAL_FLOW')

        if not query:
            return Response({'error': 'Query is required'}, status=400)

        ai_response, retrieved_chunks = generate_socratic_guidance(query, subject, topic_slug, cognitive_state)

        return Response({
            'query': query,
            'subject': subject,
            'topic_slug': topic_slug,
            'cognitive_state': cognitive_state,
            'response': ai_response,
            'retrieved_chunks': retrieved_chunks
        })

class RecordTelemetryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        subject = request.data.get('subject', 'verbal')
        topic_slug = request.data.get('topic_slug', 'general')
        cognitive_state = request.data.get('cognitive_state', 'OPTIMAL_FLOW')
        wpm = float(request.data.get('wpm', 0.0))
        backspace_count = int(request.data.get('backspace_count', 0))
        pause_duration_ms = int(request.data.get('pause_duration_ms', 0))

        user = request.user

        TelemetryLog.objects.create(
            user=user,
            subject=subject,
            topic_slug=topic_slug,
            cognitive_state=cognitive_state,
            wpm=wpm,
            backspace_count=backspace_count,
            pause_duration_ms=pause_duration_ms
        )

        # Update BKT Mastery
        tracker, created = StudentBKTTracker.objects.get_or_create(
            user=user, subject=subject, topic_slug=topic_slug
        )
        # Bayesian update formula
        if cognitive_state == 'OPTIMAL_FLOW' or wpm > 40:
            tracker.mastery_probability = min(1.0, tracker.mastery_probability + (1 - tracker.mastery_probability) * 0.15)
        elif cognitive_state == 'COGNITIVE_OVERLOAD':
            tracker.mastery_probability = max(0.05, tracker.mastery_probability * 0.85)
        tracker.review_count += 1
        tracker.save()
        mastery = tracker.mastery_probability

        return Response({
            'status': 'success',
            'cognitive_state': cognitive_state,
            'mastery_probability': round(mastery, 3)
        })


class PDFDocumentUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not _is_admin(request.user):
            return Response({'error': 'Admin access required'}, status=403)

        uploaded_file = request.FILES.get('file')
        subject = request.data.get('subject', 'general')
        topic_slug = request.data.get('topic_slug', 'custom-document')

        if not uploaded_file:
            return Response({'error': 'No file uploaded'}, status=400)

        filename = uploaded_file.name
        file_text = ""

        # Extract text from PDF / TXT file
        if filename.endswith('.pdf'):
            try:
                import pypdf
                reader = pypdf.PdfReader(uploaded_file)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        file_text += text + "\n"
            except Exception as e:
                logger.warning("PDF extraction failed, falling back to raw text: %s", e)
                file_text = uploaded_file.read().decode('utf-8', errors='ignore')
        else:
            file_text = uploaded_file.read().decode('utf-8', errors='ignore')

        if not file_text.strip():
            return Response({'error': 'Could not extract text from document.'}, status=400)

        # Create parent Document record
        doc_obj, _ = Document.objects.get_or_create(
            title=filename,
            file_name=filename,
            subject=subject,
            topic_slug=topic_slug,
            uploaded_by=request.user
        )

        # Chunk document text and create DocumentChunk vectors
        chunk_size = 400
        overlap = 50
        chunks_created = []
        start = 0
        idx = 0

        while start < len(file_text):
            end = min(start + chunk_size, len(file_text))
            chunk_str = file_text[start:end]
            vec = get_text_embedding(chunk_str)

            # Estimate page number (approx 1500 chars per page)
            estimated_page = (start // 1500) + 1

            c_obj = DocumentChunk.objects.create(
                document=doc_obj,
                subject=subject,
                topic_slug=topic_slug,
                chapter_title=filename,
                chunk_index=idx,
                content=chunk_str,
                vector_json=vec,
                metadata={'page': estimated_page, 'filename': filename}
            )
            chunks_created.append(c_obj)
            idx += 1
            start += (chunk_size - overlap)

        return Response({
            'message': f'Successfully indexed "{filename}" into {len(chunks_created)} vector concept chunks!',
            'filename': filename,
            'chunk_count': len(chunks_created)
        })

class AITutorChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        messages = request.data.get('messages', [])
        user_query = request.data.get('query', '')
        subject = request.data.get('subject', 'general')
        topic_slug = request.data.get('topic_slug', '')
        cognitive_state = request.data.get('cognitive_state', 'OPTIMAL_FLOW')

        if not user_query and messages:
            user_query = messages[-1].get('content', '')

        if not user_query:
            return Response({'error': 'Query or chat message required'}, status=400)

        ai_response, retrieved_chunks = generate_socratic_guidance(user_query, subject, topic_slug, cognitive_state)

        return Response({
            'response': ai_response,
            'retrieved_chunks': retrieved_chunks,
            'cognitive_state': cognitive_state
        })


class DocumentListDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not _is_admin(request.user):
            return Response({'error': 'Admin access required'}, status=403)

        docs = Document.objects.all().order_by('-created_at')
        result = []
        for doc in docs:
            result.append({
                'id': doc.id,
                'title': doc.title,
                'file_name': doc.file_name,
                'subject': doc.subject,
                'topic_slug': doc.topic_slug,
                'chunk_count': doc.chunks.count(),
                'created_at': doc.created_at
            })
        return Response(result)

    def delete(self, request, pk=None):
        if not _is_admin(request.user):
            return Response({'error': 'Admin access required'}, status=403)

        if not pk:
            doc_id = request.data.get('id')
        else:
            doc_id = pk

        try:
            doc = Document.objects.get(id=doc_id)
            title = doc.title
            chunks_deleted = doc.chunks.count()
            doc.delete()
            return Response({
                'message': f'Successfully deleted document "{title}" and all {chunks_deleted} associated RAG chunks!',
                'id': doc_id
            })
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=404)
