from rest_framework import serializers
from .models import ViolationLog

class ViolationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViolationLog
        fields = '__all__'
