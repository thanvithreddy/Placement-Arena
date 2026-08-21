"""
Admin API URL aggregator.
All endpoints here require is_admin_user() check (enforced in each view).
Mounted at: /api/admin-panel/
"""
from django.urls import path
from exams.views import (
    AdminExamListView, AdminExamDetailView, CreateTodayExamView,
    AdminAttemptListView, AdminAttemptDetailView, PurgeExamCountView
)
from questions.views import (
    BulkImportView, QuestionBankView, QuestionCreateView, AdminQuestionDetailView,
    PurgeAllDataView, PurgeQuestionsView, PurgeSubmissionsView,
    PurgeExamCountView as QuestionPurgeExamCountView, PurgeExamsView
)
from coding.views import AdminCodingProblemView, AdminCodingProblemDetailView, AdminTestCaseView, BulkImportCodingView
from warnings_log.views import AdminViolationListView, AdminViolationDetailView
from authentication.views import AdminUserListView, AdminUserDetailView, AdminConfirmUserView

urlpatterns = [
    # Exam management
    path('exams/', AdminExamListView.as_view(), name='admin_exam_list'),
    path('exams/create-today/', CreateTodayExamView.as_view(), name='admin_create_today_exam'),
    path('exams/<int:id>/', AdminExamDetailView.as_view(), name='admin_exam_detail'),
    path('exams/<int:id>/reset-count/', PurgeExamCountView.as_view(), name='admin_exam_reset_count'),
    path('attempts/', AdminAttemptListView.as_view(), name='admin_attempt_list'),
    path('attempts/<int:id>/', AdminAttemptDetailView.as_view(), name='admin_attempt_detail'),

    # Question bank & Selective / Bulk Purging
    path('questions/', QuestionBankView.as_view(), name='admin_question_bank'),
    path('questions/create/', QuestionCreateView.as_view(), name='admin_question_create'),
    path('questions/<int:id>/', AdminQuestionDetailView.as_view(), name='admin_question_detail'),
    path('questions/import/', BulkImportView.as_view(), name='admin_question_import'),
    path('questions/purge/', PurgeAllDataView.as_view(), name='admin_purge_data'),
    path('questions/purge-questions/', PurgeQuestionsView.as_view(), name='admin_purge_questions'),
    path('questions/purge-submissions/', PurgeSubmissionsView.as_view(), name='admin_purge_submissions'),
    path('questions/purge-exam-count/', QuestionPurgeExamCountView.as_view(), name='admin_purge_exam_count'),
    path('questions/purge-exams/', PurgeExamsView.as_view(), name='admin_purge_exams'),

    # Coding problems
    path('coding/', AdminCodingProblemView.as_view(), name='admin_coding_problems'),
    path('coding/import/', BulkImportCodingView.as_view(), name='admin_coding_import'),
    path('coding/<int:id>/', AdminCodingProblemDetailView.as_view(), name='admin_coding_detail'),
    path('coding/<int:id>/test-cases/', AdminTestCaseView.as_view(), name='admin_test_cases'),

    # User Management
    path('users/', AdminUserListView.as_view(), name='admin_user_list'),
    path('users/<int:id>/', AdminUserDetailView.as_view(), name='admin_user_detail'),
    path('users/<int:id>/confirm/', AdminConfirmUserView.as_view(), name='admin_user_confirm'),

    # Violations
    path('violations/', AdminViolationListView.as_view(), name='admin_violations'),
    path('violations/<int:id>/', AdminViolationDetailView.as_view(), name='admin_violation_detail'),
]
