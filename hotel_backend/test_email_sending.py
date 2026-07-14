import os
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_backend.settings')
django.setup()

from django.contrib.auth.models import User
from rooms.models import Room
from bookings.models import Booking

def verify_email():
    print("Starting verification...")
    # Get or create necessary objects
    user, _ = User.objects.get_or_create(username='testuser_email_test_2', defaults={'email': 'test2@example.com'})
    room = Room.objects.first()
    if not room:
        room = Room.objects.create(name='Test Room 2', price_per_night=100, capacity=2, size=20)

    # Create Booking
    b = Booking.objects.create(
        user=user,
        room=room,
        check_in=date(2026, 7, 1),
        check_out=date(2026, 7, 5),
        guest_name='Test Guest 2',
        guest_email='guest2@example.com',
        confirmed=False
    )

    print(f"Created Booking {b.id}, confirmed={b.confirmed}")

    # Confirm it
    print("Confirming booking...")
    b.confirmed = True
    b.save()
    print("Booking confirmed. Expecting email output below:")

if __name__ == "__main__":
    verify_email()
