from rest_framework import serializers
from .models import Room, RoomFeature

class RoomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFeature
        fields = ['id', 'room', 'title', 'image_url', 'description']

class RoomSerializer(serializers.ModelSerializer):
    features = RoomFeatureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Room
        fields = '__all__'