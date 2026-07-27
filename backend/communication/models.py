from django.db import models
from django.conf import settings


class SpeechTopic(models.Model):
    CATEGORY_CHOICES = [
        ('hr', 'HR Interview'),
        ('jam', 'JAM (Just A Minute)'),
        ('gd', 'Group Discussion'),
        ('custom', 'Custom'),
    ]
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='hr')
    description = models.TextField(blank=True, help_text="Optional hint or context for the topic")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"

    class Meta:
        ordering = ['category', 'title']


class SpeechAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='speech_attempts')
    topic = models.ForeignKey(SpeechTopic, on_delete=models.SET_NULL, null=True, blank=True)
    custom_topic = models.CharField(max_length=300, blank=True)  # If user typed custom topic

    # Raw transcript from speech recognition
    transcript = models.TextField()

    # Timing
    duration_seconds = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)
    wpm = models.FloatField(default=0)  # Words Per Minute

    # AI Scores (0-100)
    grammar_score = models.FloatField(default=0)
    fluency_score = models.FloatField(default=0)
    vocabulary_score = models.FloatField(default=0)
    overall_score = models.FloatField(default=0)  # out of 10

    # AI Feedback
    filler_count = models.IntegerField(default=0)
    filler_words_found = models.JSONField(default=list)  # e.g. ["um", "like", "basically"]
    corrected_transcript = models.TextField(blank=True)  # Placement-grade rewrite
    grammar_errors = models.JSONField(default=list)  # List of {original, corrected, type}
    vocabulary_upgrades = models.JSONField(default=list)  # List of {original, upgrade, reason}
    tips = models.JSONField(default=list)  # List of actionable tips

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        topic_label = self.topic.title if self.topic else self.custom_topic or "Custom"
        return f"{self.user.username} - {topic_label} ({self.overall_score}/10)"

    class Meta:
        ordering = ['-created_at']
