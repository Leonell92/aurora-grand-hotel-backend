from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Booking
from .serializers import BookingSerializer

@method_decorator(csrf_exempt, name='dispatch')
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Require authentication by default
    
    def get_queryset(self):
        """
        Users can only see their own bookings.
        This is a critical security feature!
        """
        if self.request.user.is_authenticated:
            return Booking.objects.filter(user=self.request.user)
        return Booking.objects.none()
    
    def get_permissions(self):
        """
        Allow public access to check_availability action.
        All other actions require authentication.
        """
        if self.action == 'check_availability':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def create(self, request, *args, **kwargs):
        """Create a new booking and automatically assign it to the logged-in user"""
        print("=" * 50)
        print("BOOKING REQUEST RECEIVED")
        print(f"User authenticated: {request.user.is_authenticated}")
        print(f"User: {request.user}")
        print(f"Session key: {request.session.session_key}")
        print(f"Data: {request.data}")
        print("=" * 50)
        
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required. Please log in.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Add the user to the booking data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save with the current user
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        """Automatically set the user when creating a booking"""
        print(f"Saving booking for user: {self.request.user.email}")
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def check_availability(self, request):
        """
        Check if a room is available for given dates.
        This endpoint is PUBLIC - no authentication required.
        """
        room_id = request.query_params.get('room_id')
        check_in = request.query_params.get('check_in')
        check_out = request.query_params.get('check_out')
        
        print(f"Checking availability for room {room_id}: {check_in} to {check_out}")
        
        if not all([room_id, check_in, check_out]):
            return Response(
                {'error': 'Missing required parameters'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Check for overlapping bookings
            overlapping = Booking.objects.filter(
                room_id=room_id,
                check_out__gt=check_in,
                check_in__lt=check_out
            ).exists()
            
            available = not overlapping
            print(f"Room available: {available}")
            
            return Response({
                'available': available,
                'message': 'Room is available' if available else 'Room is not available for these dates'
            })
        except Exception as e:
            print(f"Error checking availability: {str(e)}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )