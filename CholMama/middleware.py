from django.http import JsonResponse
from auth_app.models import UserAccount

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip token validation for public endpoints (e.g., login, register)
        if request.path in ['/auth/login/', '/auth/register/', '/']:
            return self.get_response(request)

        # Get token from Authorization header
        token = request.headers.get('Authorization')

        if not token:
            return JsonResponse({"error": "Authorization token is required"}, status=401)

        try:
            # Validate token and fetch user
            user = UserAccount.objects.get(token=token, is_active=True)
            # Attach the user to the request object for use in views
            request.user = user
        except UserAccount.DoesNotExist:
            return JsonResponse({"error": "Invalid or expired token"}, status=401)

        # Proceed to the next middleware or the view
        return self.get_response(request)
