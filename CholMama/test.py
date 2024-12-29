# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# # Custom manager for LoginUser (Renamed to RegisterUserManager)
# class RegisterUserManager(BaseUserManager):
#     def create_user(self, email, password, phone=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, phone=phone, **extra_fields)
#         user.set_password(password)  # Hash the password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password, phone=None, **extra_fields):
#         extra_fields.setdefault('is_admin', True)
#         return self.create_user(email, password, phone, **extra_fields)

# # Table 1: User Information
# class UserInfo(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     nid_number = models.CharField(max_length=20, unique=True)
#     phone = models.CharField(max_length=15, unique=True)

#     def __str__(self):
#         return self.username

# # Table 2: Login Information (Using RegisterUserManager)
# class LoginUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)  # Used for login
#     phone = models.CharField(max_length=15, blank=True, null=True)  # Optional for login
#     password = models.CharField(max_length=128)  # Hashed password
#     is_admin = models.BooleanField(default=False)
#     creation_date = models.DateTimeField(auto_now_add=True)
#     last_modified_date = models.DateTimeField(auto_now=True)

#     objects = RegisterUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email
