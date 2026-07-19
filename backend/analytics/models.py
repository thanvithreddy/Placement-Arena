from django.db import models

class UserAnalytics(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    exam_attempt = models.OneToOneField('exams.ExamAttempt', on_delete=models.CASCADE)
    arithmetic_accuracy = models.FloatField(default=0)
    verbal_accuracy = models.FloatField(default=0)
    reasoning_accuracy = models.FloatField(default=0)
    coding_accuracy = models.FloatField(default=0)
    weak_areas = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
