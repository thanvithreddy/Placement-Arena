from django.contrib import admin
from .models import Question, Option, Answer, SectionQuestionAssignment


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'difficulty', 'text_preview', 'marks', 'is_active']
    list_filter = ['category', 'difficulty', 'is_active']
    search_fields = ['text']
    inlines = [OptionInline]

    def text_preview(self, obj):
        return obj.text[:80] + '...' if len(obj.text) > 80 else obj.text
    text_preview.short_description = 'Question'


class SectionQuestionAssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_attempt', 'question', 'order']
    list_filter = ['section_attempt__section__section_type']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(SectionQuestionAssignment, SectionQuestionAssignmentAdmin)
