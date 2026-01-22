from django.contrib import admin
from .models import Room, RoomFeature

class RoomFeatureInline(admin.TabularInline):
    model = RoomFeature
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_per_night", "available")
    list_filter = ("available",)
    search_fields = ("name",)
    inlines = [RoomFeatureInline]

@admin.register(RoomFeature)
class RoomFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "room", "image_url")
