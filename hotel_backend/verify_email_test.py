from django.contrib.auth.models import User
from rooms.models import Room
from bookings.models import Booking
from datetime import date
import random

# Get or create necessary objects
user, _ = User.objects.get_or_create(username='testuser_email_test', defaults={'email': 'test@example.com'})
room = Room.objects.first()
if not room:
    room = Room.objects.create(name='Test Room', price_per_night=100, capacity=2, size=20)

# Create Booking
b = Booking.objects.create(
    user=user,
    room=room,
    check_in=date(2026, 6, 1),
    check_out=date(2026, 6, 5),
    guest_name='Test Guest',
    guest_email='guest@example.com',
    confirmed=False
)

print(f"Created Booking {b.id}, confirmed={b.confirmed}")

# Confirm it
print("Confirming booking...")
b.confirmed = True
b.save()
print("Booking confirmed. Check above for email output.")
