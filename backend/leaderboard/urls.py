from django.urls import path
from .views import DailyLeaderboardView, WeeklyLeaderboardView, MonthlyLeaderboardView, OverallLeaderboardView

urlpatterns = [
    path('daily/', DailyLeaderboardView.as_view(), name='daily_leaderboard'),
    path('weekly/', WeeklyLeaderboardView.as_view(), name='weekly_leaderboard'),
    path('monthly/', MonthlyLeaderboardView.as_view(), name='monthly_leaderboard'),
    path('overall/', OverallLeaderboardView.as_view(), name='overall_leaderboard'),
]
