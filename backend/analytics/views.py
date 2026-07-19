from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserAnalytics
from .serializers import UserAnalyticsSerializer
from exams.models import ExamAttempt

class MyAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        analytics = UserAnalytics.objects.filter(user=request.user).order_by('-created_at')[:30]
        return Response(UserAnalyticsSerializer(analytics, many=True).data)

class SubmissionHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        attempts = ExamAttempt.objects.filter(user=request.user).order_by('-started_at')
        result = []
        for att in attempts:
            from leaderboard.models import DailyLeaderboard
            lb = DailyLeaderboard.objects.filter(exam=att.exam, user=request.user).first()
            result.append({
                'exam_id': att.exam_id,
                'exam_title': att.exam.title,
                'exam_date': att.exam.date,
                'status': att.status,
                'total_score': att.total_score,
                'rank': lb.rank if lb else None,
                'started_at': att.started_at,
                'submitted_at': att.submitted_at,
                'time_taken_seconds': int((att.submitted_at - att.started_at).total_seconds()) if att.started_at and att.submitted_at else None
            })
        return Response(result)
