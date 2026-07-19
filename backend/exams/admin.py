from django.contrib import admin
from .models import Exam, ExamSection, ExamAttempt, SectionAttempt

admin.site.register(Exam)
admin.site.register(ExamSection)
admin.site.register(ExamAttempt)
admin.site.register(SectionAttempt)
