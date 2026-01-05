from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def register_user(request):
    """Register a new user"""
    try:
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not all([first_name, last_name, email, password]):
            return Response(
                {'error': 'All fields are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'User with this email already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validate_password(password)
        except ValidationError as e:
            return Response(
                {'error': list(e.messages)},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return Response(
            {
                'message': 'User created successfully',
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            },
            status=status.HTTP_201_CREATED
        )

    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@csrf_exempt
@api_view(['POST'])
def login_user(request):
    """Login user and create session"""
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        print("=" * 50)
        print("LOGIN ATTEMPT")
        print(f"Email: {email}")
        print(f"Session key before: {request.session.session_key}")
        print("=" * 50)

        if not email or not password:
            return Response(
                {'error': 'Email and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response(
                {'error': 'Invalid email or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Create session
        login(request, user)
        
        print("=" * 50)
        print("LOGIN SUCCESS")
        print(f"User: {user.email}")
        print(f"Session key after: {request.session.session_key}")
        print(f"Is authenticated: {user.is_authenticated}")
        print("=" * 50)

        return Response(
            {
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print(f"LOGIN ERROR: {str(e)}")
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@csrf_exempt
@api_view(['POST'])
def logout_user(request):
    """Logout user and destroy session"""
    try:
        logout(request)
        return Response(
            {'message': 'Logout successful'},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def check_auth_status(request):
    """Check if user is authenticated - for debugging"""
    return Response({
        'authenticated': request.user.is_authenticated,
        'user': {
            'id': request.user.id if request.user.is_authenticated else None,
            'email': request.user.email if request.user.is_authenticated else None,
            'username': request.user.username if request.user.is_authenticated else None,
        },
        'session_key': request.session.session_key
    })