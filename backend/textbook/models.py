from django.db import models
from django.conf import settings

class Document(models.Model):
    title = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=50) # 'verbal', 'aptitude', 'java', 'reasoning'
    topic_slug = models.CharField(max_length=100, default='general')
    file_path = models.CharField(max_length=500, blank=True, null=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.subject.upper()}] {self.title} ({self.file_name})"

class DocumentChunk(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chunks', null=True, blank=True)
    subject = models.CharField(max_length=50)
    topic_slug = models.CharField(max_length=100)
    chapter_title = models.CharField(max_length=255, default='General Document Chunk')
    chunk_index = models.IntegerField(default=0)
    content = models.TextField() # Raw chunk text
    vector_json = models.JSONField(default=list) # Vector embedding list
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chunk #{self.chunk_index} of {self.document.title if self.document else self.subject}"

# Legacy compatibility alias
TextbookChunk = DocumentChunk

class StudentBKTTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bkt_trackers')
    subject = models.CharField(max_length=50)
    topic_slug = models.CharField(max_length=100)
    mastery_probability = models.FloatField(default=0.1)
    last_reviewed_at = models.DateTimeField(auto_now=True)
    review_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'subject', 'topic_slug')

class TelemetryLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='telemetry_logs', null=True, blank=True)
    subject = models.CharField(max_length=50)
    topic_slug = models.CharField(max_length=100)
    cognitive_state = models.CharField(max_length=50)
    wpm = models.FloatField(default=0.0)
    backspace_count = models.IntegerField(default=0)
    pause_duration_ms = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
