from rest_framework import serializers
from .models import Exam, ExamSection, ExamAttempt, SectionAttempt


class ExamSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSection
        fields = ['id', 'section_type', 'order', 'duration_minutes', 'max_score', 'question_count']


class ExamSerializer(serializers.ModelSerializer):
    sections = ExamSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'date', 'status', 'description', 'created_at', 'sections']


class SectionAttemptSerializer(serializers.ModelSerializer):
    # Flat fields from related section for easy JS access
    section_type = serializers.CharField(source='section.section_type', read_only=True)
    section_order = serializers.IntegerField(source='section.order', read_only=True)
    duration_minutes = serializers.IntegerField(source='section.duration_minutes', read_only=True)
    max_score = serializers.IntegerField(source='section.max_score', read_only=True)
    question_count = serializers.IntegerField(source='section.question_count', read_only=True)

    class Meta:
        model = SectionAttempt
        fields = [
            'id', 'section_id', 'section_type', 'section_order',
            'duration_minutes', 'max_score', 'question_count',
            'status', 'score', 'started_at', 'submitted_at', 'is_auto_submitted'
        ]


class ExamAttemptSerializer(serializers.ModelSerializer):
    section_attempts = SectionAttemptSerializer(many=True, read_only=True)
    class Meta:
        model = ExamAttempt
        fields = ['id', 'user_id', 'exam_id', 'status', 'total_score', 'violations_count', 'started_at', 'submitted_at', 'section_attempts']
