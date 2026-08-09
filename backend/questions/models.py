from django.db import models

class Question(models.Model):
    DIFFICULTY_CHOICES = [('easy','Easy'),('medium','Medium'),('hard','Hard')]
    section = models.ForeignKey('exams.ExamSection', on_delete=models.CASCADE, related_name='questions', null=True, blank=True)
    category = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    text = models.TextField()
    explanation = models.TextField(blank=True)
    marks = models.FloatField(default=4.0)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

class Answer(models.Model):
    section_attempt = models.ForeignKey('exams.SectionAttempt', related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    marks_awarded = models.FloatField(default=0)
    answered_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ['section_attempt', 'question']

class SectionQuestionAssignment(models.Model):
    """
    Randomized question pool assigned to a specific SectionAttempt.
    Created once when a section is started. Enables different users to
    get different (randomized) sets of questions from the same question bank.
    """
    section_attempt = models.ForeignKey(
        'exams.SectionAttempt',
        related_name='question_assignments',
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)  # randomized display order

    class Meta:
        unique_together = ['section_attempt', 'question']
        ordering = ['order']




class JavaTopic(models.Model):
    order = models.IntegerField(unique=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=150)
    concept_summary = models.TextField()
    syntax_rules = models.JSONField(default=list)  # List of syntax rules & compiler traps
    code_example = models.TextField()  # Runnable Java code snippet
    memory_diagram_json = models.JSONField(default=dict)  # Stack/Heap layout
    common_errors = models.JSONField(default=list)  # Common compilation errors
    xp_reward = models.IntegerField(default=100)
    quiz_json = models.JSONField(default=list)  # Challenge questions

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"


class UserJavaProgress(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    java_topic = models.ForeignKey(JavaTopic, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    xp_earned = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'java_topic']


class UserGamificationProfile(models.Model):
    user = models.OneToOneField('authentication.User', related_name='gamification_profile', on_delete=models.CASCADE)
    total_xp = models.IntegerField(default=0)
    current_level = models.IntegerField(default=1)
    streak_days = models.IntegerField(default=1)
    last_activity_date = models.DateField(auto_now=True)
    badges_json = models.JSONField(default=list)

