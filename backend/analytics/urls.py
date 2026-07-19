from django.urls import path
from .views import MyAnalyticsView, SubmissionHistoryView

urlpatterns = [
    path('me/', MyAnalyticsView.as_view(), name='my_analytics'),
    path('history/', SubmissionHistoryView.as_view(), name='submission_history'),
]
