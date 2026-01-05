from django.contrib import admin
from .models import Room  # import your Room model

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_per_night", "available")
    list_filter = ("available",)
    search_fields = ("name",)

