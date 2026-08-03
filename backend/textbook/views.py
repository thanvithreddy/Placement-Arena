from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import TextbookChunk, StudentBKTTracker, TelemetryLog
from .serializers import TextbookChunkSerializer, StudentBKTTrackerSerializer
from .rag_engine import get_text_embedding, generate_socratic_guidance

class IngestTextbookView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    def post(self, request):
        subject = request.data.get('subject', 'verbal')
        topic_slug = request.data.get('topic_slug', 'general')
        cognitive_state = request.data.get('cognitive_state', 'OPTIMAL_FLOW')
        wpm = float(request.data.get('wpm', 0.0))
        backspace_count = int(request.data.get('backspace_count', 0))
        pause_duration_ms = int(request.data.get('pause_duration_ms', 0))

        user = request.user if request.user.is_authenticated else None

        TelemetryLog.objects.create(
            user=user,
            subject=subject,
            topic_slug=topic_slug,
            cognitive_state=cognitive_state,
            wpm=wpm,
            backspace_count=backspace_count,
            pause_duration_ms=pause_duration_ms
        )

        # Update BKT Mastery if user authenticated
        mastery = 0.5
        if user:
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
