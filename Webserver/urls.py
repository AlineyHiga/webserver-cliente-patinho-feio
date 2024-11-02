# main/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import (
    register_user,
    login_user,
    logout_user
)

urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)