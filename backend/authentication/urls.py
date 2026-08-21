from django.urls import path
from .views import LoginView, SignUpView, LogoutView, MeView, TokenRefreshView, StreakView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
    path('streak/', StreakView.as_view(), name='streak'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
