from django.db import models

class DailyLeaderboard(models.Model):
    exam = models.ForeignKey('exams.Exam', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    total_score = models.FloatField(default=0)
    time_taken_seconds = models.IntegerField(default=0)
    arithmetic_score = models.FloatField(default=0)
    verbal_score = models.FloatField(default=0)
    reasoning_score = models.FloatField(default=0)
    coding_score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['exam', 'user']
        ordering = ['rank']
