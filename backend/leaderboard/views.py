from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import DailyLeaderboard
from .serializers import DailyLeaderboardSerializer
from exams.models import Exam, ExamAttempt
from datetime import date

def update_leaderboard(exam):
    # Include completed and in-progress attempts for real-time live ranking
    attempts = ExamAttempt.objects.filter(exam=exam).exclude(status='not_started')
    
    attempt_list = []
    for att in attempts:
        time_taken = 0
        if att.started_at and att.submitted_at:
            time_taken = (att.submitted_at - att.started_at).total_seconds()
            
        # Calculate section scores
        arithmetic = 0
        verbal = 0
        reasoning = 0
        coding = 0
        
        for sa in att.section_attempts.all():
            if sa.section.section_type == 'arithmetic': arithmetic = sa.score
            elif sa.section.section_type == 'verbal': verbal = sa.score
            elif sa.section.section_type == 'reasoning': reasoning = sa.score
            elif sa.section.section_type == 'coding': coding = sa.score
            
        attempt_list.append({
            'user': att.user,
            'total_score': att.total_score,
            'time_taken': time_taken,
            'arithmetic': arithmetic,
            'verbal': verbal,
            'reasoning': reasoning,
            'coding': coding
        })
        
    attempt_list.sort(key=lambda x: (-x['total_score'], x['time_taken']))
    
    for i, data in enumerate(attempt_list):
        DailyLeaderboard.objects.update_or_create(
            exam=exam,
            user=data['user'],
            defaults={
                'rank': i + 1,
                'total_score': data['total_score'],
                'time_taken_seconds': data['time_taken'],
                'arithmetic_score': data['arithmetic'],
                'verbal_score': data['verbal'],
                'reasoning_score': data['reasoning'],
                'coding_score': data['coding']
            }
        )

class DailyLeaderboardView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        exam_id = request.query_params.get('exam_id')
        if exam_id:
            try:
                exam = Exam.objects.get(id=exam_id)
            except Exam.DoesNotExist:
                return Response({'error': 'Exam not found'}, status=404)
        else:
            # Get today's exam or latest active/completed exam
            exam = Exam.objects.filter(date=date.today()).first() or Exam.objects.order_by('-date').first()
            if not exam:
                return Response([])
                
        # Update leaderboard in real-time
        update_leaderboard(exam)
        
        lb = DailyLeaderboard.objects.filter(exam=exam).order_by('rank')
        return Response(DailyLeaderboardSerializer(lb, many=True).data)

class WeeklyLeaderboardView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        from datetime import date, timedelta
        from django.db.models import Sum, Avg, Count
        from authentication.models import User
        
        week_ago = date.today() - timedelta(days=7)
        entries = DailyLeaderboard.objects.filter(exam__date__gte=week_ago).values('user').annotate(
            total=Sum('total_score'),
            exams=Count('id'),
            avg_score=Avg('total_score')
        ).order_by('-total')
        
        result = []
        for i, entry in enumerate(entries):
            user = User.objects.get(id=entry['user'])
            result.append({
                'rank': i + 1,
                'username': user.username,
                'display_name': user.display_name or user.username,
                'total_score': entry['total'],
                'exams_taken': entry['exams'],
                'avg_score': round(entry['avg_score'], 1)
            })
        return Response(result)

class MonthlyLeaderboardView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        from datetime import date, timedelta
        from django.db.models import Sum, Avg, Count
        from authentication.models import User
        
        month_ago = date.today() - timedelta(days=30)
        entries = DailyLeaderboard.objects.filter(exam__date__gte=month_ago).values('user').annotate(
            total=Sum('total_score'),
            exams=Count('id'),
            avg_score=Avg('total_score')
        ).order_by('-total')
        
        result = []
        for i, entry in enumerate(entries):
            user = User.objects.get(id=entry['user'])
            result.append({
                'rank': i + 1,
                'username': user.username,
                'display_name': user.display_name or user.username,
                'total_score': entry['total'],
                'exams_taken': entry['exams'],
                'avg_score': round(entry['avg_score'], 1)
            })
        return Response(result)

class OverallLeaderboardView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        from django.db.models import Sum, Avg, Count
        from authentication.models import User
        
        entries = DailyLeaderboard.objects.values('user').annotate(
            total=Sum('total_score'),
            exams=Count('id'),
            avg_score=Avg('total_score')
        ).order_by('-total')
        
        result = []
        for i, entry in enumerate(entries):
            user = User.objects.get(id=entry['user'])
            result.append({
                'rank': i + 1,
                'username': user.username,
                'display_name': user.display_name or user.username,
                'total_score': entry['total'],
                'exams_taken': entry['exams'],
                'avg_score': round(entry['avg_score'], 1)
            })
        return Response(result)
