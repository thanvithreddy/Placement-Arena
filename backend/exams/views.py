from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Exam, ExamSection, ExamAttempt, SectionAttempt
from .serializers import ExamSerializer, ExamAttemptSerializer, SectionAttemptSerializer
from datetime import date
from django.utils import timezone

class TodayExamView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        exam = Exam.objects.filter(date=date.today(), status='active').first()
        if not exam:
            return Response({'message': 'No active exam today'}, status=status.HTTP_404_NOT_FOUND)
            
        attempt = ExamAttempt.objects.filter(user=request.user, exam=exam).first()
        data = {
            'exam': ExamSerializer(exam).data,
            'attempt': ExamAttemptSerializer(attempt).data if attempt else None
        }
        return Response(data)

class ExamDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try:
            exam = Exam.objects.get(id=id)
            return Response(ExamSerializer(exam).data)
        except Exam.DoesNotExist:
            return Response({'error': 'Exam not found'}, status=status.HTTP_404_NOT_FOUND)

class StartExamView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        try:
            exam = Exam.objects.get(id=id)
        except Exam.DoesNotExist:
            return Response({'error': 'Exam not found'}, status=status.HTTP_404_NOT_FOUND)
            
        attempt, created = ExamAttempt.objects.get_or_create(
            user=request.user,
            exam=exam,
            defaults={'status': 'in_progress', 'started_at': timezone.now()}
        )
        
        if created:
            for section in exam.sections.all():
                SectionAttempt.objects.create(
                    exam_attempt=attempt,
                    section=section
                )
                
        return Response(ExamAttemptSerializer(attempt).data, status=status.HTTP_200_OK)

class StartSectionView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, section_id):
        try:
            section_attempt = SectionAttempt.objects.get(
                id=section_id, 
                exam_attempt__user=request.user
            )
        except SectionAttempt.DoesNotExist:
            return Response({'error': 'Section attempt not found'}, status=status.HTTP_404_NOT_FOUND)
            
        if section_attempt.status == 'not_started':
            section_attempt.status = 'in_progress'
            section_attempt.started_at = timezone.now()
            section_attempt.save()
            
            # --- Question Randomization ---
            # Only assign questions if not already assigned (idempotent)
            from questions.models import Question, SectionQuestionAssignment
            if not section_attempt.question_assignments.exists():
                section = section_attempt.section
                section_type = section.section_type
                count = section.question_count
                
                # Try section-specific questions first (legacy), then fall back to bank
                qs = list(Question.objects.filter(
                    section=section, is_active=True
                ))
                
                if len(qs) < count:
                    # Pull from question bank by matching category
                    category_map = {
                        'arithmetic': 'arithmetic',
                        'verbal': 'verbal',
                        'reasoning': 'reasoning',
                    }
                    bank_category = category_map.get(section_type)
                    if bank_category:
                        bank_qs = list(Question.objects.filter(
                            section__isnull=True,
                            category=bank_category,
                            is_active=True
                        ).exclude(id__in=[q.id for q in qs]))
                        qs = qs + bank_qs
                
                # Shuffle and cap to question_count
                import random
                random.shuffle(qs)
                selected = qs[:count]
                
                for i, q in enumerate(selected):
                    SectionQuestionAssignment.objects.get_or_create(
                        section_attempt=section_attempt,
                        question=q,
                        defaults={'order': i + 1}
                    )
            
        return Response(SectionAttemptSerializer(section_attempt).data)


class SubmitSectionView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, section_id):
        try:
            section_attempt = SectionAttempt.objects.get(
                id=section_id, 
                exam_attempt__user=request.user
            )
        except SectionAttempt.DoesNotExist:
            return Response({'error': 'Section attempt not found'}, status=status.HTTP_404_NOT_FOUND)
            
        section_attempt.status = 'completed'
        section_attempt.submitted_at = timezone.now()
        
        # Calculate score (for MCQ sections)
        score = 0
        if section_attempt.section.section_type != 'coding':
            for answer in section_attempt.answers.all():
                if answer.is_correct:
                    score += answer.marks_awarded
        
        # For coding, score is updated by coding submissions
        if section_attempt.section.section_type != 'coding':
            section_attempt.score = score
            
        section_attempt.save()
        
        # Check if all sections are completed
        exam_attempt = section_attempt.exam_attempt
        all_sections = exam_attempt.section_attempts.all()
        if all(s.status == 'completed' for s in all_sections):
            exam_attempt.status = 'completed'
            exam_attempt.submitted_at = timezone.now()
            exam_attempt.total_score = sum(s.score for s in all_sections)
            exam_attempt.save()
            
            # Leaderboard and analytics updates
            from leaderboard.views import update_leaderboard
            update_leaderboard(exam_attempt.exam)
            
            def compute_analytics(exam_attempt):
                from analytics.models import UserAnalytics
                from questions.models import Answer
                
                totals = {'arithmetic': [0,0], 'verbal': [0,0], 'reasoning': [0,0]}
                
                for sa in exam_attempt.section_attempts.all():
                    cat = sa.section.section_type
                    if cat in totals:
                        answers = sa.answers.all()
                        totals[cat][1] += answers.count()
                        totals[cat][0] += answers.filter(is_correct=True).count()
                
                def acc(correct, total):
                    return round((correct / total * 100), 1) if total > 0 else 0.0
                
                weak = [k for k, v in totals.items() if v[1] > 0 and (v[0]/v[1]) < 0.6]
                
                UserAnalytics.objects.update_or_create(
                    exam_attempt=exam_attempt,
                    defaults={
                        'user': exam_attempt.user,
                        'arithmetic_accuracy': acc(*totals['arithmetic']),
                        'verbal_accuracy': acc(*totals['verbal']),
                        'reasoning_accuracy': acc(*totals['reasoning']),
                        'coding_accuracy': 0.0,  # updated separately on coding submit
                        'weak_areas': weak
                    }
                )
            compute_analytics(exam_attempt)
            
        return Response(SectionAttemptSerializer(section_attempt).data)

class ExamResultView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, exam_id):
        try:
            attempt = ExamAttempt.objects.get(exam_id=exam_id, user=request.user)
        except ExamAttempt.DoesNotExist:
            return Response({'error': 'Attempt not found'}, status=404)
        
        sections_data = []
        for sa in attempt.section_attempts.order_by('section__order'):
            answered = sa.answers.count()
            correct = sa.answers.filter(is_correct=True).count()
            sections_data.append({
                'section_type': sa.section.section_type,
                'order': sa.section.order,
                'duration_minutes': sa.section.duration_minutes,
                'max_score': sa.section.max_score,
                'question_count': sa.section.question_count,
                'score': sa.score,
                'answered': answered,
                'correct': correct,
                'status': sa.status,
                'is_auto_submitted': sa.is_auto_submitted,
            })
        
        # Get leaderboard rank
        from leaderboard.models import DailyLeaderboard
        lb_entry = DailyLeaderboard.objects.filter(exam_id=exam_id, user=request.user).first()
        rank = lb_entry.rank if lb_entry else None
        
        time_taken = None
        if attempt.started_at and attempt.submitted_at:
            time_taken = int((attempt.submitted_at - attempt.started_at).total_seconds())
        
        return Response({
            'exam_id': exam_id,
            'exam_title': attempt.exam.title,
            'status': attempt.status,
            'total_score': attempt.total_score,
            'rank': rank,
            'time_taken_seconds': time_taken,
            'sections': sections_data
        })

class AdminExamListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        exams = Exam.objects.all()
        return Response(ExamSerializer(exams, many=True).data)
        
    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminExamDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, id):
        try:
            return Exam.objects.get(id=id)
        except Exam.DoesNotExist:
            return None
            
    def get(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        exam = self.get_object(id)
        if not exam:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(ExamSerializer(exam).data)
        
    def put(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        exam = self.get_object(id)
        if not exam:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExamSerializer(exam, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        exam = self.get_object(id)
        if not exam:
            return Response(status=status.HTTP_404_NOT_FOUND)
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateTodayExamView(APIView):
    """
    POST /api/admin-panel/exams/create-today/
    Creates an exam for today with all 4 standard sections.
    Returns existing exam if one already exists for today.
    """
    permission_classes = [IsAuthenticated]

    SECTION_DEFAULTS = [
        {'section_type': 'arithmetic', 'order': 1, 'duration_minutes': 20, 'max_score': 100, 'question_count': 25},
        {'section_type': 'verbal',     'order': 2, 'duration_minutes': 20, 'max_score': 80,  'question_count': 20},
        {'section_type': 'reasoning',  'order': 3, 'duration_minutes': 20, 'max_score': 100, 'question_count': 25},
        {'section_type': 'coding',     'order': 4, 'duration_minutes': 60, 'max_score': 200, 'question_count': 2},
    ]

    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

        today = date.today()
        existing = Exam.objects.filter(date=today).first()
        if existing:
            return Response(
                {**ExamSerializer(existing).data, 'already_existed': True},
                status=status.HTTP_200_OK
            )

        title = request.data.get('title') or f'Daily Practice — {today.strftime("%d %b %Y")}'

        exam = Exam.objects.create(
            title=title,
            date=today,
            status='active',
            created_by=request.user,
            description=f'Placement practice exam for {today.strftime("%d %B %Y")}.'
        )

        for section_data in self.SECTION_DEFAULTS:
            ExamSection.objects.create(exam=exam, **section_data)

        return Response(ExamSerializer(exam).data, status=status.HTTP_201_CREATED)

