# hotel_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Aurora Grand Hotel API</h1><p>Go to the frontend at <a href='http://localhost:8080'>http://localhost:8080</a></p>")

urlpatterns = [
    path('', home, name='home'),  # ← Add this line
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')),  # your API
    path('api/', include('rooms.urls')),   # if you have a separate rooms app
]