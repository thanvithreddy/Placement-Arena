from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView
import os

# Serve frontend HTML files directly from Django
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'frontend')
FRONTEND_DIR = os.path.normpath(FRONTEND_DIR)

urlpatterns = [
    # Root redirect to login page
    path('', RedirectView.as_view(url='/login/index.html', permanent=False)),
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/auth/', include('authentication.urls')),
    path('api/exams/', include('exams.urls')),
    path('api/questions/', include('questions.urls')),
    path('api/coding/', include('coding.urls')),
    path('api/leaderboard/', include('leaderboard.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/violations/', include('warnings_log.urls')),
    path('api/admin-panel/', include('placement_arena.admin_api_urls')),

    # Serve frontend HTML files (excluding api, admin, static, media paths)
    re_path(r'^(?!(api|admin|static|media)/)(?P<path>.*)$', serve, {'document_root': FRONTEND_DIR, 'show_indexes': False}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
