from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking

@receiver(post_save, sender=Booking)
def send_confirmation_email(sender, instance, created, **kwargs):
    if instance.confirmed:
        # Check if we should send email
        subject = f'Booking Confirmation - Booking #{instance.id}'
        message = f'Hi {instance.guest_name},\n\nYour booking at Aurora Grand Hotel is confirmed.\n\nRoom: {instance.room.name}\nDates: {instance.check_in} to {instance.check_out}\n\nThank you!'
        recipient_list = [instance.guest_email]
        
        # Helper to print to console so we definitely see it in development even without backend fully configured sometimes
        print(f"Sending email to {instance.guest_email}: {subject}")
        
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
