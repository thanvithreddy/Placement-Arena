from rest_framework import serializers
from .models import ViolationLog

class ViolationLogSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    user_display_name = serializers.ReadOnlyField(source='user.display_name')

    class Meta:
        model = ViolationLog
        fields = ['id', 'user', 'user_username', 'user_display_name', 'exam_attempt', 'violation_type', 'timestamp', 'description']
