from django.db import models

ROOM_TYPES = [
    ('single', 'Single'),
    ('double', 'Double'),
    ('suite', 'Suite'),
]

class Room(models.Model):
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    max_guests = models.IntegerField(default=2)
    image_url = models.URLField(blank=True, null=True)
    amenities = models.JSONField(blank=True, null=True)
    available = models.BooleanField(default=True)      # ADD THIS

    def __str__(self):
        return f"{self.name} - {self.room_type}"