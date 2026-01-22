from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rooms.views import RoomViewSet, RoomFeatureViewSet
from bookings.views import BookingViewSet
from bookings.auth_views import register_user, login_user, logout_user, check_auth_status

# Create ONE router for all ViewSets
router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'room-features', RoomFeatureViewSet, basename='room-feature')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # All API endpoints
    path('api/auth/register/', register_user, name='register'),
    path('api/auth/login/', login_user, name='login'),
    path('api/auth/logout/', logout_user, name='logout'),
    path('api/auth/status/', check_auth_status, name='auth-status'),
]