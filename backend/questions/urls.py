from django.urls import path
from .views import (
    SectionQuestionsView, SaveAnswerView,
    BulkImportView, QuestionBankView, QuestionCreateView
)

urlpatterns = [
    path('section/<int:section_id>/', SectionQuestionsView.as_view(), name='section_questions'),
    path('save-answer/', SaveAnswerView.as_view(), name='save_answer'),
    
    # Admin URLs
    path('admin/import/', BulkImportView.as_view(), name='import_questions'),
    path('admin/', QuestionBankView.as_view(), name='question_bank'),
    path('admin/create/', QuestionCreateView.as_view(), name='create_question'),
]
