from django.db import models

class CodingProblem(models.Model):
    section = models.ForeignKey('exams.ExamSection', on_delete=models.CASCADE, related_name='coding_problems', null=True, blank=True)
    title = models.CharField(max_length=200)
    statement = models.TextField()
    constraints = models.TextField(blank=True)
    input_format = models.TextField(blank=True)
    output_format = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=[('easy','Easy'),('medium','Medium'),('hard','Hard')], default='medium')
    time_limit_ms = models.IntegerField(default=5000)
    memory_limit_mb = models.IntegerField(default=256)
    max_score = models.IntegerField(default=100)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class SampleTestCase(models.Model):
    problem = models.ForeignKey(CodingProblem, related_name='sample_cases', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()
    explanation = models.TextField(blank=True)
    order = models.IntegerField(default=1)

class HiddenTestCase(models.Model):
    problem = models.ForeignKey(CodingProblem, related_name='hidden_cases', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()
    score_weight = models.FloatField(default=1.0)
    order = models.IntegerField(default=1)

class CodingSubmission(models.Model):
    LANGUAGE_CHOICES = [('python','Python'),('java','Java'),('cpp','C++'),('c','C')]
    STATUS_CHOICES = [('pending','Pending'),('running','Running'),('accepted','Accepted'),('wrong_answer','Wrong Answer'),('runtime_error','Runtime Error'),('time_limit_exceeded','TLE'),('compilation_error','CE')]
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    exam_attempt = models.ForeignKey('exams.ExamAttempt', on_delete=models.CASCADE, null=True, blank=True)
    problem = models.ForeignKey(CodingProblem, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    code = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    score = models.FloatField(default=0)
    passed_sample = models.IntegerField(default=0)
    total_sample = models.IntegerField(default=0)
    passed_hidden = models.IntegerField(default=0)
    total_hidden = models.IntegerField(default=0)
    execution_time_ms = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_final = models.BooleanField(default=False)
