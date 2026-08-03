from django.db import models
from django.conf import settings

class TextbookChunk(models.Model):
    subject = models.CharField(max_length=50) # e.g. 'verbal', 'aptitude', 'java'
    topic_slug = models.CharField(max_length=100) # e.g. 'subject-verb-agreement'
    chapter_title = models.CharField(max_length=255, default='General Notes')
    chunk_index = models.IntegerField(default=0)
    content = models.TextField() # Raw textbook text snippet
    vector_json = models.JSONField(default=list) # 1536-dim or 384-dim vector list
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.topic_slug} (Chunk #{self.chunk_index})"

class StudentBKTTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bkt_trackers')
    subject = models.CharField(max_length=50)
    topic_slug = models.CharField(max_length=100)
    mastery_probability = models.FloatField(default=0.1) # p(Lt)
    last_reviewed_at = models.DateTimeField(auto_now=True)
    review_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'subject', 'topic_slug')

class TelemetryLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='telemetry_logs', null=True, blank=True)
    subject = models.CharField(max_length=50)
    topic_slug = models.CharField(max_length=100)
    cognitive_state = models.CharField(max_length=50) # 'COGNITIVE_OVERLOAD', 'UNDER_STIMULATED', 'OPTIMAL_FLOW'
    wpm = models.FloatField(default=0.0)
    backspace_count = models.IntegerField(default=0)
    pause_duration_ms = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
