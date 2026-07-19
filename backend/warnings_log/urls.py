from django.urls import path
from .views import LogViolationView, AdminViolationListView

urlpatterns = [
    path('log/', LogViolationView.as_view(), name='log_violation'),
    path('admin/', AdminViolationListView.as_view(), name='admin_violations'),
]
