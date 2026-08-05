from django.urls import path
from .views import (
    CodingProblemView, CodingProblemsListView, RunCodeView, SubmitCodeView,
    CodingHistoryView
)

urlpatterns = [
    path('problems/', CodingProblemsListView.as_view(), name='coding_problems_list'),
    path('problem/<int:id>/', CodingProblemView.as_view(), name='coding_problem'),
    path('run/', RunCodeView.as_view(), name='run_code'),
    path('submit/', SubmitCodeView.as_view(), name='submit_code'),
    path('history/<int:problem_id>/', CodingHistoryView.as_view(), name='coding_history'),
]

