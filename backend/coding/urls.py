from django.urls import path
from .views import (
    CodingProblemView, CodingProblemsListView, RunCodeView, SubmitCodeView,
    CodingHistoryView, AdminCodingProblemView, AdminCodingProblemDetailView,
    AdminTestCaseView
)

urlpatterns = [
    path('problems/', CodingProblemsListView.as_view(), name='coding_problems_list'),
    path('problem/<int:id>/', CodingProblemView.as_view(), name='coding_problem'),
    path('run/', RunCodeView.as_view(), name='run_code'),
    path('submit/', SubmitCodeView.as_view(), name='submit_code'),
    path('history/<int:problem_id>/', CodingHistoryView.as_view(), name='coding_history'),

    # Admin URLs
    path('admin/', AdminCodingProblemView.as_view(), name='admin_coding_problems'),
    path('admin/<int:id>/', AdminCodingProblemDetailView.as_view(), name='admin_coding_detail'),
    path('admin/<int:id>/test-cases/', AdminTestCaseView.as_view(), name='admin_test_cases'),
]
