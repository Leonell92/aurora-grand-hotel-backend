from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Room
from .serializers import RoomSerializer

@method_decorator(csrf_exempt, name='dispatch')
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer