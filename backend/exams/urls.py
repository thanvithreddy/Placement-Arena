from django.urls import path
from .views import (
    TodayExamView, ExamDetailView, StartExamView,
    StartSectionView, SubmitSectionView, ExamResultView, ExamReviewView,
    AdminExamListView, AdminExamDetailView, CreateTodayExamView, ResetDuplicateAttemptView
)

urlpatterns = [
    path('today/', TodayExamView.as_view(), name='today_exam'),
    path('<int:id>/', ExamDetailView.as_view(), name='exam_detail'),
    path('<int:id>/start/', StartExamView.as_view(), name='start_exam'),
    path('attempts/<int:id>/reset-on-duplicate/', ResetDuplicateAttemptView.as_view(), name='reset_duplicate_attempt'),
    path('sections/<int:section_id>/start/', StartSectionView.as_view(), name='start_section'),
    path('sections/<int:section_id>/submit/', SubmitSectionView.as_view(), name='submit_section'),
    path('<int:exam_id>/result/', ExamResultView.as_view(), name='exam_result'),
    path('<int:exam_id>/review/', ExamReviewView.as_view(), name='exam_review'),
]
