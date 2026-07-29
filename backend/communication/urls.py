from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.TopicListView.as_view(), name='speech-topics'),
    path('analyze/', views.AnalyzeSpeechView.as_view(), name='analyze-speech'),
    path('history/', views.SpeechHistoryView.as_view(), name='speech-history'),
    path('history/purge/', views.PurgeHistoryView.as_view(), name='speech-history-purge'),
    path('translate/', views.TranslateView.as_view(), name='translate'),
    path('admin/topics/', views.AdminTopicView.as_view(), name='admin-topics'),
    path('admin/topics/<int:pk>/', views.AdminTopicDetailView.as_view(), name='admin-topic-detail'),
    path('admin/attempts/', views.AdminAttemptsView.as_view(), name='admin-attempts'),
]
