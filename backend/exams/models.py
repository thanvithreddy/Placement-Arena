from django.db import models

class Exam(models.Model):
    STATUS_CHOICES = [('draft','Draft'),('active','Active'),('completed','Completed')]
    title = models.CharField(max_length=200)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ExamSection(models.Model):
    SECTION_TYPES = [('arithmetic','Arithmetic'),('verbal','Verbal'),('reasoning','Reasoning'),('coding','Coding')]
    exam = models.ForeignKey(Exam, related_name='sections', on_delete=models.CASCADE)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    order = models.IntegerField()  # 1,2,3,4
    duration_minutes = models.IntegerField()
    max_score = models.IntegerField()
    question_count = models.IntegerField()

class ExamAttempt(models.Model):
    STATUS_CHOICES = [('not_started','Not Started'),('in_progress','In Progress'),('completed','Completed')]
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    total_score = models.FloatField(default=0)
    violations_count = models.IntegerField(default=0)
    class Meta:
        unique_together = ['user', 'exam']

class SectionAttempt(models.Model):
    exam_attempt = models.ForeignKey(ExamAttempt, related_name='section_attempts', on_delete=models.CASCADE)
    section = models.ForeignKey(ExamSection, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(default=0)
    is_auto_submitted = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='not_started')  # not_started, in_progress, completed
