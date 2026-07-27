from rest_framework import serializers
from .models import SpeechTopic, SpeechAttempt


class SpeechTopicSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = SpeechTopic
        fields = ['id', 'title', 'category', 'category_display', 'description', 'is_active', 'created_at']


class SpeechAttemptSerializer(serializers.ModelSerializer):
    topic_title = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    display_name = serializers.CharField(source='user.display_name', read_only=True)

    class Meta:
        model = SpeechAttempt
        fields = [
            'id', 'user', 'username', 'display_name', 'topic', 'topic_title', 'custom_topic',
            'transcript', 'duration_seconds', 'word_count', 'wpm',
            'grammar_score', 'fluency_score', 'vocabulary_score', 'overall_score',
            'filler_count', 'filler_words_found', 'corrected_transcript',
            'grammar_errors', 'vocabulary_upgrades', 'tips', 'created_at'
        ]
        read_only_fields = ['user', 'created_at']

    def get_topic_title(self, obj):
        if obj.topic:
            return obj.topic.title
        return obj.custom_topic or 'Custom Topic'


class SpeechAttemptCreateSerializer(serializers.Serializer):
    topic_id = serializers.IntegerField(required=False, allow_null=True)
    custom_topic = serializers.CharField(required=False, allow_blank=True, default='')
    transcript = serializers.CharField()
    duration_seconds = serializers.IntegerField(min_value=0)
