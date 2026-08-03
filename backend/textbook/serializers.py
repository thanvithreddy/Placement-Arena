from rest_framework import serializers
from .models import TextbookChunk, StudentBKTTracker, TelemetryLog

class TextbookChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextbookChunk
        fields = ['id', 'subject', 'topic_slug', 'chapter_title', 'chunk_index', 'content', 'metadata', 'created_at']

class StudentBKTTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBKTTracker
        fields = ['id', 'subject', 'topic_slug', 'mastery_probability', 'last_reviewed_at', 'review_count']
