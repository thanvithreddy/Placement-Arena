from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import ViolationLog
from .serializers import ViolationLogSerializer
from exams.models import ExamAttempt
from django.utils import timezone

class LogViolationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        exam_attempt_id = request.data.get('exam_attempt_id')
        violation_type = request.data.get('violation_type')
        description = request.data.get('description', '')
        
        try:
            attempt = ExamAttempt.objects.get(id=exam_attempt_id, user=request.user)
        except ExamAttempt.DoesNotExist:
            return Response({'error': 'Invalid exam attempt'}, status=status.HTTP_400_BAD_REQUEST)
            
        ViolationLog.objects.create(
            user=request.user,
            exam_attempt=attempt,
            violation_type=violation_type,
            description=description
        )
        
        attempt.violations_count += 1
        attempt.save()
        
        auto_submitted = False
        if attempt.violations_count >= 3 and violation_type in ['tab_switch', 'fullscreen_exit']:
            attempt.status = 'completed'
            attempt.submitted_at = timezone.now()
            attempt.save()
            # Also complete active sections
            for sa in attempt.section_attempts.filter(status='in_progress'):
                sa.status = 'completed'
                sa.is_auto_submitted = True
                sa.submitted_at = timezone.now()
                sa.save()
            auto_submitted = True
            
        return Response({
            'warning_count': attempt.violations_count,
            'auto_submitted': auto_submitted
        })

class AdminViolationListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if not request.user.is_admin_user():
            return Response(status=status.HTTP_403_FORBIDDEN)
        logs = ViolationLog.objects.all().order_by('-timestamp')
        return Response(ViolationLogSerializer(logs, many=True).data)
