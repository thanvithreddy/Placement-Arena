from rest_framework import serializers
from .models import DailyLeaderboard

class DailyLeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    display_name = serializers.CharField(source='user.display_name', read_only=True)
    
    class Meta:
        model = DailyLeaderboard
        fields = '__all__'
