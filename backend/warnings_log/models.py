from django.db import models

class ViolationLog(models.Model):
    VIOLATION_TYPES = [
        ('fullscreen_exit', 'Fullscreen Exit'),
        ('tab_switch', 'Tab Switch'),
        ('right_click', 'Right Click Attempt'),
        ('keyboard_shortcut', 'Keyboard Shortcut'),
        ('copy_paste', 'Copy/Paste Attempt'),
    ]
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    exam_attempt = models.ForeignKey('exams.ExamAttempt', on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=30, choices=VIOLATION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True)
