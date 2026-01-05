from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    # Make user read-only so it can't be set from the frontend
    user = serializers.ReadOnlyField(source='user.id')
    user_name = serializers.ReadOnlyField(source='user.get_full_name')
    room_name = serializers.ReadOnlyField(source='room.name')
    
    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'user_name',
            'room',
            'room_name',
            'check_in',
            'check_out',
            'guest_name',
            'guest_email',
            'guests',
            'created_at',
            'confirmed'
        ]
        read_only_fields = ['id', 'user', 'user_name', 'room_name', 'created_at']