from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'room', 
        'guest_name', 
        'guest_email', 
        'check_in', 
        'check_out', 
        'guests', 
        'confirmed', 
        'created_at'
    )
    list_filter = ('confirmed', 'check_in', 'check_out', 'created_at')
    search_fields = ('guest_name', 'guest_email', 'room__name')
    list_editable = ('confirmed',)  # Allow editing confirmed status directly in list view
    date_hierarchy = 'check_in'
    ordering = ('-created_at',)
    
    # Custom admin actions
    actions = ['confirm_bookings', 'unconfirm_bookings']
    
    def confirm_bookings(self, request, queryset):
        """Mark selected bookings as confirmed"""
        updated = queryset.update(confirmed=True)
        self.message_user(
            request, 
            f'{updated} booking(s) successfully confirmed.'
        )
    confirm_bookings.short_description = "✓ Confirm selected bookings"
    
    def unconfirm_bookings(self, request, queryset):
        """Mark selected bookings as pending"""
        updated = queryset.update(confirmed=False)
        self.message_user(
            request, 
            f'{updated} booking(s) marked as pending.'
        )
    unconfirm_bookings.short_description = "⏳ Mark selected bookings as pending"
    
    # Customize the detail view
    fieldsets = (
        ('Booking Information', {
            'fields': ('room', 'check_in', 'check_out', 'guests')
        }),
        ('Guest Information', {
            'fields': ('user', 'guest_name', 'guest_email')
        }),
        ('Status', {
            'fields': ('confirmed', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'user')