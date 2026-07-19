from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Question, Option, Answer, SectionQuestionAssignment
from .serializers import QuestionSerializer, AnswerSerializer, AdminQuestionSerializer
from exams.models import SectionAttempt
import openpyxl


class SectionQuestionsView(APIView):
    """
    Returns questions for a section attempt.
    Uses SectionQuestionAssignment for randomized questions.
    Falls back to direct section assignment for legacy data.
    Also includes each question's saved answer for session restore.
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, section_id):
        try:
            attempt = SectionAttempt.objects.get(id=section_id, exam_attempt__user=request.user)
        except SectionAttempt.DoesNotExist:
            return Response({'error': 'Unauthorized or section not found'}, status=status.HTTP_403_FORBIDDEN)
        
        # Try randomized assignments first (Phase 3)
        assignments = attempt.question_assignments.select_related('question').order_by('order')
        
        if assignments.exists():
            questions = [a.question for a in assignments]
        else:
            # Legacy: direct section assignment
            questions = list(Question.objects.filter(section=attempt.section, is_active=True).order_by('order'))
        
        # Build a lookup of saved answers for session restore
        saved_answers = {
            ans.question_id: ans.selected_option_id
            for ans in Answer.objects.filter(section_attempt=attempt)
        }
        
        # Serialize with saved answer
        result = []
        for q in questions:
            q_data = QuestionSerializer(q).data
            q_data['saved_option_id'] = saved_answers.get(q.id)  # None if not answered yet
            result.append(q_data)
        
        return Response(result)


class SaveAnswerView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        try:
            attempt = SectionAttempt.objects.get(id=data.get('section_attempt_id'), exam_attempt__user=request.user)
        except SectionAttempt.DoesNotExist:
            return Response({'error': 'Invalid section attempt'}, status=status.HTTP_400_BAD_REQUEST)
            
        if attempt.status == 'completed':
            return Response({'error': 'Section already submitted'}, status=status.HTTP_400_BAD_REQUEST)
            
        question_id = data.get('question_id')
        option_id = data.get('option_id')
        
        try:
            question = Question.objects.get(id=question_id)
            option = Option.objects.get(id=option_id, question=question) if option_id else None
        except (Question.DoesNotExist, Option.DoesNotExist):
            return Response({'error': 'Invalid question or option'}, status=status.HTTP_400_BAD_REQUEST)
            
        is_correct = option.is_correct if option else False
        marks_awarded = question.marks if is_correct else 0
        
        answer, created = Answer.objects.update_or_create(
            section_attempt=attempt,
            question=question,
            defaults={
                'selected_option': option,
                'is_correct': is_correct,
                'marks_awarded': marks_awarded
            }
        )
        return Response(AnswerSerializer(answer).data)


class BulkImportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
            
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            wb = openpyxl.load_workbook(file_obj)
        except Exception as e:
            return Response({'error': f'Invalid Excel file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        
        sheet = wb.active
        count = 0
        errors = []
        
        for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
            if not row[2]:  # Question text empty
                continue
            try:
                category = str(row[0]).lower().strip() if row[0] else 'arithmetic'
                difficulty = str(row[1]).lower().strip() if row[1] else 'medium'
                q_text = str(row[2]).strip()
                opts = [row[3], row[4], row[5], row[6]]
                correct_opt_char = str(row[7]).upper().strip() if row[7] else 'A'
                explanation = str(row[8]).strip() if row[8] else ''
                marks = float(row[9]) if row[9] else 4.0
                
                q = Question.objects.create(
                    category=category,
                    difficulty=difficulty,
                    text=q_text,
                    explanation=explanation,
                    marks=marks
                )
                
                correct_index = ord(correct_opt_char[0]) - 65
                for i, opt_text in enumerate(opts):
                    if opt_text:
                        Option.objects.create(
                            question=q,
                            text=str(opt_text).strip(),
                            is_correct=(i == correct_index),
                            order=i + 1
                        )
                count += 1
            except Exception as e:
                errors.append(f'Row {row_num}: {str(e)}')
            
        return Response({
            'message': f'Successfully imported {count} questions',
            'errors': errors
        })


class QuestionBankView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
        category = request.query_params.get('category')
        difficulty = request.query_params.get('difficulty')
        
        qs = Question.objects.all()
        if category:
            qs = qs.filter(category=category)
        if difficulty:
            qs = qs.filter(difficulty=difficulty)
        
        return Response(AdminQuestionSerializer(qs, many=True).data)


class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        serializer = AdminQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
