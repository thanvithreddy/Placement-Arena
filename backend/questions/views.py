from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Question, Option, Answer, SectionQuestionAssignment
from .serializers import QuestionSerializer, AnswerSerializer, AdminQuestionSerializer
from exams.models import SectionAttempt
import openpyxl
import csv
import io


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
            
        filename = file_obj.name.lower()
        rows = []

        # Support both CSV and Excel (.xlsx, .xls) formats
        if filename.endswith('.csv') or 'csv' in file_obj.content_type:
            try:
                content = file_obj.read()
                try:
                    decoded = content.decode('utf-8-sig')
                except UnicodeDecodeError:
                    decoded = content.decode('latin-1')
                
                reader = csv.reader(io.StringIO(decoded))
                rows = list(reader)
            except Exception as e:
                return Response({'error': f'Failed to parse CSV file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                wb = openpyxl.load_workbook(file_obj, data_only=True)
                sheet = wb.active
                rows = list(sheet.iter_rows(values_only=True))
            except Exception as e:
                return Response({'error': f'Failed to parse Excel file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
            
        if not rows:
            return Response({'error': 'Uploaded file is empty'}, status=status.HTTP_400_BAD_REQUEST)
            
        count = 0
        errors = []
        
        # Check if first row is header
        start_idx = 1 if len(rows) > 0 and str(rows[0][0]).strip().lower() in ['category', 'cat', 'q_category'] else 0

        def clean_val(val):
            if val is None:
                return ""
            s = str(val).strip()
            # Clean common broken encoding artifacts (e.g. â‚¹ -> ₹)
            s = s.replace('â‚¹', '₹').replace('â€™', "'").replace('â€"', "-")
            return s

        for i, row in enumerate(rows[start_idx:], start=start_idx + 1):
            if not row or len(row) < 4:
                continue

            # Convert row to strings
            r = [clean_val(cell) for cell in row]

            cat = r[0].lower() if r[0] else 'arithmetic'
            if cat not in ['arithmetic', 'verbal', 'reasoning']:
                cat = 'arithmetic'
                
            diff = r[1].lower() if len(r) > 1 and r[1] else 'medium'
            if diff not in ['easy', 'medium', 'hard']:
                diff = 'medium'

            q_text = r[2] if len(r) > 2 else ''
            if not q_text:
                continue

            opt_a = r[3] if len(r) > 3 else ''
            opt_b = r[4] if len(r) > 4 else ''
            opt_c = r[5] if len(r) > 5 else ''
            opt_d = r[6] if len(r) > 6 else ''
            correct_raw = r[7].upper() if len(r) > 7 else 'A'
            exp = r[8] if len(r) > 8 else ''
            
            try:
                marks = float(r[9]) if len(r) > 9 and r[9] else 4.0
            except ValueError:
                marks = 4.0

            # Determine correct option index
            correct_idx = 0
            if correct_raw in ['A', '1', 'OPTION A', 'OPTION_A']:
                correct_idx = 0
            elif correct_raw in ['B', '2', 'OPTION B', 'OPTION_B']:
                correct_idx = 1
            elif correct_raw in ['C', '3', 'OPTION C', 'OPTION_C']:
                correct_idx = 2
            elif correct_raw in ['D', '4', 'OPTION D', 'OPTION_D']:
                correct_idx = 3

            question = Question.objects.create(
                category=cat,
                difficulty=diff,
                text=q_text,
                explanation=exp,
                marks=marks
            )

            opts = [opt_a, opt_b, opt_c, opt_d]
            for idx, opt_text in enumerate(opts):
                if opt_text:
                    Option.objects.create(
                        question=question,
                        text=opt_text,
                        is_correct=(idx == correct_idx),
                        order=idx + 1
                    )
            count += 1

        return Response({
            'message': f'Successfully imported {count} questions!',
            'errors': errors
        })


class QuestionBankView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
        category = request.query_params.get('category')
        difficulty = request.query_params.get('difficulty')
        
        qs = Question.objects.all().order_by('-id')
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


class PurgeAllDataView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

        from warnings_log.models import ViolationLog
        from coding.models import CodingSubmission, CodingProblem, SampleTestCase, HiddenTestCase
        from exams.models import Exam, ExamSection, ExamAttempt, SectionAttempt
        from leaderboard.models import DailyLeaderboard
        from analytics.models import UserAnalytics

        ViolationLog.objects.all().delete()
        CodingSubmission.objects.all().delete()
        Answer.objects.all().delete()
        SectionAttempt.objects.all().delete()
        ExamAttempt.objects.all().delete()
        DailyLeaderboard.objects.all().delete()
        UserAnalytics.objects.all().delete()
        Option.objects.all().delete()
        Question.objects.all().delete()
        SampleTestCase.objects.all().delete()
        HiddenTestCase.objects.all().delete()
        CodingProblem.objects.all().delete()
        ExamSection.objects.all().delete()
        Exam.objects.all().delete()

        return Response({'message': 'All questions, exams, submissions, and logs have been completely purged!'})
