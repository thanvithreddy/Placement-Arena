from django.contrib import admin
from .models import SpeechTopic, SpeechAttempt


@admin.register(SpeechTopic)
class SpeechTopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['title']


@admin.register(SpeechAttempt)
class SpeechAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'overall_score', 'wpm', 'filler_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'transcript']
    readonly_fields = ['user', 'transcript', 'corrected_transcript', 'grammar_errors',
                       'vocabulary_upgrades', 'filler_words_found', 'tips']
