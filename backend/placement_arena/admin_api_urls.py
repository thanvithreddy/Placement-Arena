"""
Admin API URL aggregator.
All endpoints here require is_admin_user() check (enforced in each view).
Mounted at: /api/admin-panel/
"""
from django.urls import path
from exams.views import AdminExamListView, AdminExamDetailView, CreateTodayExamView, AdminAttemptListView
from questions.views import BulkImportView, QuestionBankView, QuestionCreateView, PurgeAllDataView
from coding.views import AdminCodingProblemView, AdminCodingProblemDetailView, AdminTestCaseView, BulkImportCodingView
from warnings_log.views import AdminViolationListView

urlpatterns = [
    # Exam management
    path('exams/', AdminExamListView.as_view(), name='admin_exam_list'),
    path('exams/create-today/', CreateTodayExamView.as_view(), name='admin_create_today_exam'),
    path('exams/<int:id>/', AdminExamDetailView.as_view(), name='admin_exam_detail'),
    path('attempts/', AdminAttemptListView.as_view(), name='admin_attempt_list'),

    # Question bank & Purge
    path('questions/', QuestionBankView.as_view(), name='admin_question_bank'),
    path('questions/create/', QuestionCreateView.as_view(), name='admin_question_create'),
    path('questions/import/', BulkImportView.as_view(), name='admin_question_import'),
    path('questions/purge/', PurgeAllDataView.as_view(), name='admin_purge_data'),

    # Coding problems
    path('coding/', AdminCodingProblemView.as_view(), name='admin_coding_problems'),
    path('coding/import/', BulkImportCodingView.as_view(), name='admin_coding_import'),
    path('coding/<int:id>/', AdminCodingProblemDetailView.as_view(), name='admin_coding_detail'),
    path('coding/<int:id>/test-cases/', AdminTestCaseView.as_view(), name='admin_test_cases'),

    # Violations
    path('violations/', AdminViolationListView.as_view(), name='admin_violations'),
]
