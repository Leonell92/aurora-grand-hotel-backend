from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    Session authentication without CSRF enforcement.
    Use this for API endpoints where CSRF protection is handled differently.
    """
    def enforce_csrf(self, request):
        return  # Skip CSRF check