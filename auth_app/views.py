from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserAccount, UserProfile
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
import uuid


############################################
#   Handling User Registration
############################################
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validate required fields
            required_fields = ['email', 'password', 'name', 'nid_number', 'phone']
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse({"error": f"{field} is required"}, status=400)

            # Extract data
            email = data['email']
            password = data['password']
            name = data['name']  # Changed from 'username' to 'name'
            nid_number = data['nid_number']
            phone = data['phone']

            # Validate email format
            try:
                validate_email(email)
            except ValidationError:
                return JsonResponse({"error": "Invalid email format"}, status=400)

            # Check if email or phone already exists
            if UserAccount.objects.filter(email=email).exists() or UserProfile.objects.filter(phone=phone).exists():
                return JsonResponse({"error": "Email or phone number already registered"}, status=400)

            # Create user account
            user = UserAccount.objects.create_user(email=email, password=password)
            # Create user profile
            UserProfile.objects.create(
                user_id=user,  # Use the UserAccount instance
                name=name,  # Changed from 'username' to 'name'
                nid_number=nid_number,
                phone=phone,
                email=email
            )

            return JsonResponse({"message": "User registered successfully"}, status=201)

        except ValidationError as ve:
            return JsonResponse({"error": ve.message}, status=400)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

############################################
#   Handling User Login
############################################
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validate required fields
            if not data.get('email') or not data.get('password'):
                return JsonResponse({"error": "Email and password are required"}, status=400)

            # Extract data
            email = data['email']
            password = data['password']

            # Authenticate user
            user = authenticate(request, email=email, password=password)
            if user:
                # if not user.is_active:
                #     return JsonResponse({"error": "This account is inactive"}, status=403)

                # Generate a new token
                new_token = str(uuid.uuid4())
                user.token = new_token
                user.save()

                return JsonResponse({"token": new_token, "message": "Login successful"}, status=200)
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)

        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)



#######
# For Testing
#######
def protected_view(request):
    user = getattr(request, 'user', None)
    if user:
        return JsonResponse({"message": f"Hello, {user.email}"}, status=200)
    return JsonResponse({"error": "Unauthorized access"}, status=401)