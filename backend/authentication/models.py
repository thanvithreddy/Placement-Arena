from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [('admin', 'Admin'), ('candidate', 'Candidate')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='candidate')
    display_name = models.CharField(max_length=100, blank=True)
    total_exams_taken = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_admin_user(self):
        return self.role == 'admin'


class DailyStreak(models.Model):
    """Tracks the daily exam streak for each candidate."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='streak')
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_exam_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} — streak: {self.current_streak}"
