from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from .auth_views import register_user, login_user, logout_user, check_auth_status

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/logout/', logout_user, name='logout'),
    path('auth/status/', check_auth_status, name='auth-status'),  # Debug endpoint
    path('', include(router.urls)),
]