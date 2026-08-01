from django.urls import path
from .views import (
    SectionQuestionsView, SaveAnswerView,
    BulkImportView, QuestionBankView, QuestionCreateView,
    AptitudeTopicsView, AptitudeQuestionsView, AptitudeSubmitAnswerView,
    JavaTopicsView, JavaTopicDetailView, JavaCompleteTopicView
)

urlpatterns = [
    path('section/<int:section_id>/', SectionQuestionsView.as_view(), name='section_questions'),
    path('save-answer/', SaveAnswerView.as_view(), name='save_answer'),

    # Aptitude Topic Mastery URLs
    path('aptitude/topics/', AptitudeTopicsView.as_view(), name='aptitude_topics'),
    path('aptitude/topics/<slug:slug>/', AptitudeQuestionsView.as_view(), name='aptitude_questions'),
    path('aptitude/submit-answer/', AptitudeSubmitAnswerView.as_view(), name='aptitude_submit'),

    # Gamified Java Mastery Quest URLs
    path('java-quest/topics/', JavaTopicsView.as_view(), name='java_quest_topics'),
    path('java-quest/topics/<slug:slug>/', JavaTopicDetailView.as_view(), name='java_quest_detail'),
    path('java-quest/topics/<slug:slug>/complete/', JavaCompleteTopicView.as_view(), name='java_quest_complete'),

    # Admin URLs
    path('admin/import/', BulkImportView.as_view(), name='import_questions'),
    path('admin/', QuestionBankView.as_view(), name='question_bank'),
    path('admin/create/', QuestionCreateView.as_view(), name='create_question'),
]
