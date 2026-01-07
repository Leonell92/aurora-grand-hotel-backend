from django.urls import path
from .auth_views import register_user, login_user, logout_user, check_auth_status

# No router here - just auth views
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('status/', check_auth_status, name='auth-status'),
]