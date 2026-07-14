#!/usr/bin/env python
"""
Script to create a separate admin superuser for Django administration.
This keeps your frontend user account separate from backend admin access.
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_backend.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User

def create_admin_user():
    """Create a dedicated admin superuser."""
    
    # Admin credentials
    username = 'hoteladmin'
    email = 'admin@aurorагrandhotel.com'  # You can change this or leave it
    password = 'AdminHotel2026!'  # CHANGE THIS to your preferred password
    
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f"❌ User '{username}' already exists!")
        user = User.objects.get(username=username)
        print(f"   Email: {user.email}")
        print(f"   Is superuser: {user.is_superuser}")
        print(f"   Is staff: {user.is_staff}")
        return
    
    # Create the superuser
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    
    print("✅ Admin superuser created successfully!")
    print(f"   Username: {username}")
    print(f"   Email: {email}")
    print(f"   Password: {password}")
    print("\n⚠️  IMPORTANT: Change the password after first login!")
    print(f"   Login at: https://aurora-grand-hotel-backend.onrender.com/admin/")

if __name__ == '__main__':
    create_admin_user()
