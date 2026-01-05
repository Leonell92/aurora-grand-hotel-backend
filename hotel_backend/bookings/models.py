from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ADD THIS - link booking to user
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guests = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']  # Show newest bookings first
    
    def __str__(self):
        return f"Booking {self.id} - {self.guest_name} - {self.room.name}"