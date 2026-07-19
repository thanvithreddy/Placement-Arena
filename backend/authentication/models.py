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
