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
        attempt = ExamAttempt.objects.filter(user=request.user, exam=exam).first() if exam else None
        data = {
            'exam': ExamSerializer(exam).data if exam else None,
            'attempt': ExamAttemptSerializer(attempt).data if attempt else None,
            'message': 'Active exam today' if exam else 'No active exam today'
        }
        return Response(data, status=status.HTTP_200_OK)

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
            
        force_reset = request.data.get('reset', False) or request.query_params.get('reset', False)
        attempt = ExamAttempt.objects.filter(user=request.user, exam=exam).first()
        
        if not attempt:
            attempt = ExamAttempt.objects.create(
                user=request.user,
                exam=exam,
                status='in_progress',
                started_at=timezone.now()
            )
            for section in exam.sections.all().order_by('order'):
                SectionAttempt.objects.create(
                    exam_attempt=attempt,
                    section=section,
                    status='not_started'
                )
        elif force_reset or attempt.status == 'completed' or not attempt.section_attempts.filter(status__in=['not_started', 'in_progress']).exists():
            # Reset attempt for a fresh exam attempt session
            attempt.section_attempts.all().delete()
            attempt.status = 'in_progress'
            attempt.started_at = timezone.now()
            attempt.submitted_at = None
            attempt.total_score = 0
            attempt.violations_count = 0
            attempt.save()

            for section in exam.sections.all().order_by('order'):
                SectionAttempt.objects.create(
                    exam_attempt=attempt,
                    section=section,
                    status='not_started'
                )

        return Response(ExamAttemptSerializer(attempt).data, status=status.HTTP_200_OK)

def seed_category_questions(category):
    from questions.models import Question, Option
    category_lower = str(category).lower()
    
    if category_lower == 'arithmetic':
        samples = [
            {
                'text': 'A train 140 m long running at 60 km/hr passes a platform in 30 seconds. What is the length of the platform?',
                'difficulty': 'medium', 'marks': 4.0, 'explanation': 'Speed in m/s = 60 * 5/18 = 50/3 m/s. Total distance = speed * time = (50/3) * 30 = 500m. Platform length = 500 - 140 = 360m.',
                'options': [
                    {'text': '360 m', 'is_correct': True},
                    {'text': '320 m', 'is_correct': False},
                    {'text': '400 m', 'is_correct': False},
                    {'text': '280 m', 'is_correct': False},
                ]
            },
            {
                'text': 'If 15 men can complete a work in 12 days, how many days will 10 men take to complete the same work?',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'Man-days required = 15 * 12 = 180. Days for 10 men = 180 / 10 = 18 days.',
                'options': [
                    {'text': '18 days', 'is_correct': True},
                    {'text': '15 days', 'is_correct': False},
                    {'text': '20 days', 'is_correct': False},
                    {'text': '24 days', 'is_correct': False},
                ]
            },
            {
                'text': 'A sum of money doubles itself at simple interest in 8 years. What is the rate of interest per annum?',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'SI = Principal P. SI = (P * R * T) / 100 => P = (P * R * 8) / 100 => R = 100 / 8 = 12.5%.',
                'options': [
                    {'text': '12.5%', 'is_correct': True},
                    {'text': '10%', 'is_correct': False},
                    {'text': '15%', 'is_correct': False},
                    {'text': '8%', 'is_correct': False},
                ]
            },
            {
                'text': 'The average of 5 consecutive numbers is 27. What is the largest of these numbers?',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'Middle number (3rd) is 27. The numbers are 25, 26, 27, 28, 29. Largest is 29.',
                'options': [
                    {'text': '29', 'is_correct': True},
                    {'text': '28', 'is_correct': False},
                    {'text': '30', 'is_correct': False},
                    {'text': '31', 'is_correct': False},
                ]
            },
            {
                'text': 'A trader marks his goods 20% above cost price and allows a discount of 10%. What is his profit percentage?',
                'difficulty': 'medium', 'marks': 4.0, 'explanation': 'Let CP = 100. MP = 120. SP = 120 - 10% of 120 = 108. Profit % = 8%.',
                'options': [
                    {'text': '8%', 'is_correct': True},
                    {'text': '10%', 'is_correct': False},
                    {'text': '12%', 'is_correct': False},
                    {'text': '6%', 'is_correct': False},
                ]
            }
        ]
    elif category_lower == 'verbal':
        samples = [
            {
                'text': 'Choose the word most nearly OPPOSITE in meaning to: CANDID',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'Candid means frank and straightforward. Deceitful is the opposite.',
                'options': [
                    {'text': 'Deceitful', 'is_correct': True},
                    {'text': 'Frank', 'is_correct': False},
                    {'text': 'Honest', 'is_correct': False},
                    {'text': 'Sincere', 'is_correct': False},
                ]
            },
            {
                'text': 'Identify the correctly spelled word:',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'Accommodation is spelled with double c and double m.',
                'options': [
                    {'text': 'Accommodation', 'is_correct': True},
                    {'text': 'Acommodate', 'is_correct': False},
                    {'text': 'Accomodation', 'is_correct': False},
                    {'text': 'Acomodation', 'is_correct': False},
                ]
            },
            {
                'text': 'Fill in the blank: She has been living in London _____ 2018.',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'Since is used for a specific point in time in perfect tenses.',
                'options': [
                    {'text': 'since', 'is_correct': True},
                    {'text': 'for', 'is_correct': False},
                    {'text': 'from', 'is_correct': False},
                    {'text': 'in', 'is_correct': False},
                ]
            },
            {
                'text': 'Select the synonym for: METICULOUS',
                'difficulty': 'medium', 'marks': 4.0, 'explanation': 'Meticulous means showing great attention to detail; careful.',
                'options': [
                    {'text': 'Careful', 'is_correct': True},
                    {'text': 'Careless', 'is_correct': False},
                    {'text': 'Hasty', 'is_correct': False},
                    {'text': 'Lazy', 'is_correct': False},
                ]
            },
            {
                'text': 'Find the error: "Neither of the two candidates have submitted their resume."',
                'difficulty': 'hard', 'marks': 4.0, 'explanation': '"Neither" takes a singular verb: "has submitted".',
                'options': [
                    {'text': 'have submitted', 'is_correct': True},
                    {'text': 'Neither of', 'is_correct': False},
                    {'text': 'the two candidates', 'is_correct': False},
                    {'text': 'their resume', 'is_correct': False},
                ]
            }
        ]
    elif category_lower == 'reasoning':
        samples = [
            {
                'text': 'Complete the series: 3, 7, 15, 31, 63, ?',
                'difficulty': 'medium', 'marks': 4.0, 'explanation': 'Pattern is x2 + 1. 63 * 2 + 1 = 127.',
                'options': [
                    {'text': '127', 'is_correct': True},
                    {'text': '125', 'is_correct': False},
                    {'text': '128', 'is_correct': False},
                    {'text': '130', 'is_correct': False},
                ]
            },
            {
                'text': 'If CAT is coded as 3120, how is DOG coded in that language?',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'Alphabet positions: C=3, A=1, T=20. D=4, O=15, G=7 -> 4157.',
                'options': [
                    {'text': '4157', 'is_correct': True},
                    {'text': '4158', 'is_correct': False},
                    {'text': '4147', 'is_correct': False},
                    {'text': '4167', 'is_correct': False},
                ]
            },
            {
                'text': 'Pointing to a photograph, a man said "I have no brother or sister but that man\'s father is my father\'s son." Whose photograph was it?',
                'difficulty': 'hard', 'marks': 4.0, 'explanation': '"My father\'s son" = the man himself. "That man\'s father is my father\'s son" = that man\'s father is the man himself. So it is his son\'s photograph.',
                'options': [
                    {'text': 'His son', 'is_correct': True},
                    {'text': 'His nephew', 'is_correct': False},
                    {'text': 'His father', 'is_correct': False},
                    {'text': 'Himself', 'is_correct': False},
                ]
            },
            {
                'text': 'If NORTH is facing UP and you turn 90 degrees clockwise, which direction are you facing?',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': '90 degrees clockwise from North is East.',
                'options': [
                    {'text': 'EAST', 'is_correct': True},
                    {'text': 'WEST', 'is_correct': False},
                    {'text': 'SOUTH', 'is_correct': False},
                    {'text': 'NORTH-EAST', 'is_correct': False},
                ]
            },
            {
                'text': 'Which number does not belong in the set: 4, 9, 16, 25, 35, 49?',
                'difficulty': 'easy', 'marks': 4.0, 'explanation': 'All are perfect squares except 35.',
                'options': [
                    {'text': '35', 'is_correct': True},
                    {'text': '25', 'is_correct': False},
                    {'text': '49', 'is_correct': False},
                    {'text': '16', 'is_correct': False},
                ]
            }
        ]
    else:
        samples = []

    for item in samples:
        q = Question.objects.create(
            category=category_lower,
            difficulty=item['difficulty'],
            text=item['text'],
            explanation=item['explanation'],
            marks=item['marks'],
            is_active=True
        )
        for idx, opt in enumerate(item['options']):
            Option.objects.create(
                question=q,
                text=opt['text'],
                is_correct=opt['is_correct'],
                order=idx + 1
            )


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
            
        from questions.models import Question, SectionQuestionAssignment
        from questions.serializers import QuestionSerializer

        if not section_attempt.question_assignments.exists():
            section = section_attempt.section
            section_type = section.section_type
            count = section.question_count
            
            # Fetch questions specifically assigned to section
            qs = list(Question.objects.filter(section=section, is_active=True))
            
            # Pull from question bank matching category case-insensitively
            bank_qs = list(Question.objects.filter(
                category__iexact=section_type,
                is_active=True
            ).exclude(id__in=[q.id for q in qs]))
            
            all_available = qs + bank_qs
            
            if not all_available and section_type in ['arithmetic', 'verbal', 'reasoning']:
                seed_category_questions(section_type)
                qs = list(Question.objects.filter(section=section, is_active=True))
                bank_qs = list(Question.objects.filter(category__iexact=section_type, is_active=True))
                all_available = qs + bank_qs

            if all_available:
                import random
                random.shuffle(all_available)
                selected = all_available[:count] if (count > 0 and len(all_available) >= count) else all_available
                
                for i, q in enumerate(selected):
                    SectionQuestionAssignment.objects.get_or_create(
                        section_attempt=section_attempt,
                        question=q,
                        defaults={'order': i + 1}
                    )

        # Get assigned questions for this section attempt
        assignments = section_attempt.question_assignments.select_related('question').order_by('order')
        if assignments.exists():
            questions = [a.question for a in assignments if a.question]
        else:
            # Fallback: get active questions matching section category case-insensitively
            questions = list(Question.objects.filter(category__iexact=section_attempt.section.section_type, is_active=True).order_by('order'))

        data = SectionAttemptSerializer(section_attempt).data
        data['questions'] = QuestionSerializer(questions, many=True).data
        return Response(data)


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


class ExamReviewView(APIView):
    """
    GET /api/exams/{id}/review/
    Returns full question-by-question review (right/wrong options, user selected options, explanations)
    for 2 hours after exam submission. Auto-deletes questions after 2 hours.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, exam_id):
        try:
            attempt = ExamAttempt.objects.get(exam_id=exam_id, user=request.user)
        except ExamAttempt.DoesNotExist:
            return Response({'error': 'Attempt not found'}, status=status.HTTP_404_NOT_FOUND)

        now = timezone.now()
        submitted_at = attempt.submitted_at or attempt.started_at or now

        elapsed_seconds = (now - submitted_at).total_seconds()
        two_hours_in_seconds = 7200 # 2 hours in seconds

        # Check if 2 hours passed since exam submission
        if elapsed_seconds > two_hours_in_seconds:
            # Auto-delete questions for sections in this exam if not deleted already
            sections = attempt.exam.sections.all()
            for sec in sections:
                sec.questions.all().delete()
                sec.coding_problems.all().delete()

            return Response({
                'expired': True,
                'message': 'The 2-hour post-exam review window has expired. Exam questions have been automatically deleted.',
                'elapsed_seconds': elapsed_seconds
            })

        # Report is active (within 2 hours)
        remaining_seconds = max(0, int(two_hours_in_seconds - elapsed_seconds))

        sections_review = []
        for sa in attempt.section_attempts.order_by('section__order'):
            sec = sa.section

            if sec.section_type == 'coding':
                from coding.models import CodingSubmission, CodingProblem
                problems_data = []
                coding_problems = sec.coding_problems.all()
                if not coding_problems.exists():
                    coding_problems = CodingProblem.objects.all()

                for cp in coding_problems:
                    sub = CodingSubmission.objects.filter(user=request.user, problem=cp).order_by('-submitted_at').first()
                    problems_data.append({
                        'problem_id': cp.id,
                        'title': cp.title,
                        'statement': cp.statement,
                        'max_score': cp.max_score,
                        'submitted_code': sub.code if sub else 'No code submitted',
                        'score': sub.score if sub else 0,
                        'passed_sample': sub.passed_sample if sub else 0,
                        'total_sample': sub.total_sample if sub else 0,
                        'passed_hidden': sub.passed_hidden if sub else 0,
                        'total_hidden': sub.total_hidden if sub else 0,
                        'status': sub.status if sub else 'not_submitted'
                    })

                sections_review.append({
                    'section_type': 'coding',
                    'order': sec.order,
                    'score': sa.score,
                    'max_score': sec.max_score,
                    'problems': problems_data
                })

            else:
                questions_data = []
                questions = sec.questions.all()
                if not questions.exists():
                    from questions.models import Question
                    questions = Question.objects.filter(category=sec.section_type)

                for q in questions:
                    ans = sa.answers.filter(question=q).first()
                    user_option_id = ans.selected_option.id if (ans and ans.selected_option) else None
                    is_correct = ans.is_correct if ans else False

                    options_data = []
                    correct_option_text = ""
                    selected_option_text = "Not Answered"

                    for opt in q.options.all():
                        options_data.append({
                            'id': opt.id,
                            'text': opt.text,
                            'is_correct': opt.is_correct
                        })
                        if opt.is_correct:
                            correct_option_text = opt.text
                        if user_option_id == opt.id:
                            selected_option_text = opt.text

                    questions_data.append({
                        'question_id': q.id,
                        'text': q.text,
                        'marks': q.marks,
                        'explanation': q.explanation,
                        'options': options_data,
                        'user_option_id': user_option_id,
                        'user_option_text': selected_option_text,
                        'correct_option_text': correct_option_text,
                        'is_correct': is_correct,
                        'status': 'correct' if is_correct else ('wrong' if user_option_id else 'unanswered')
                    })

                sections_review.append({
                    'section_type': sec.section_type,
                    'order': sec.order,
                    'score': sa.score,
                    'max_score': sec.max_score,
                    'questions': questions_data
                })

        return Response({
            'expired': False,
            'remaining_seconds': remaining_seconds,
            'exam_title': attempt.exam.title,
            'sections': sections_review
        })


class AdminExamListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        exams = Exam.objects.all().order_by('-date', '-id')
        return Response(ExamSerializer(exams, many=True).data)
        
    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

        title = request.data.get('title')
        date_val = request.data.get('date') or date.today()
        status_val = request.data.get('status', 'active')
        sections_data = request.data.get('sections', [])

        if not title:
            return Response({'error': 'Exam title is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Deactivate any existing active exam for the same date if status is active
        if status_val == 'active':
            Exam.objects.filter(date=date_val, status='active').update(status='completed')

        exam = Exam.objects.create(
            title=title,
            date=date_val,
            status=status_val,
            created_by=request.user
        )

        # Create sections if provided, or default 4 sections
        if sections_data:
            for s in sections_data:
                ExamSection.objects.create(
                    exam=exam,
                    section_type=s.get('section_type'),
                    order=s.get('order', 1),
                    duration_minutes=s.get('duration_minutes', 20),
                    max_score=s.get('max_score', 100),
                    question_count=s.get('question_count', 25)
                )
        else:
            default_sections = [
                {'section_type': 'arithmetic', 'order': 1, 'duration_minutes': 20, 'max_score': 100, 'question_count': 25},
                {'section_type': 'verbal', 'order': 2, 'duration_minutes': 20, 'max_score': 80, 'question_count': 20},
                {'section_type': 'reasoning', 'order': 3, 'duration_minutes': 20, 'max_score': 100, 'question_count': 25},
                {'section_type': 'coding', 'order': 4, 'duration_minutes': 60, 'max_score': 200, 'question_count': 2},
            ]
            for s in default_sections:
                ExamSection.objects.create(exam=exam, **s)

        return Response(ExamSerializer(exam).data, status=status.HTTP_201_CREATED)

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


class AdminAttemptListView(APIView):
    """
    GET /api/admin-panel/attempts/
    Returns all candidate exam attempts with user details, scores, violations, status, and section breakdowns.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

        attempts = ExamAttempt.objects.all().order_by('-started_at')
        result = []
        for att in attempts:
            sections_summary = []
            for sa in att.section_attempts.order_by('section__order'):
                sections_summary.append({
                    'section_type': sa.section.section_type,
                    'score': sa.score,
                    'max_score': sa.section.max_score,
                    'status': sa.status,
                    'is_auto_submitted': sa.is_auto_submitted
                })

            result.append({
                'attempt_id': att.id,
                'user_id': att.user.id,
                'username': att.user.username,
                'display_name': att.user.display_name or att.user.username,
                'exam_id': att.exam.id,
                'exam_title': att.exam.title,
                'status': att.status,
                'total_score': att.total_score,
                'violations_count': att.violations_count,
                'started_at': att.started_at,
                'submitted_at': att.submitted_at,
                'sections': sections_summary
            })
        return Response(result)


