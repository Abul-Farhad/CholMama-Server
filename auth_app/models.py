from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Custom Manager for UserAccount
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# UserAccount Table
class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)  # PK
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token = models.CharField(max_length=255, null=True, blank=True)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user_accounts'  # Custom table name
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"

    def __str__(self):
        return f"{self.email} (ID: {self.id})"


# UserProfile Table
# UserProfile Table
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)  # Explicit PK
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, db_column='user_id', null=True)  # FK to UserAccount
    name = models.CharField(max_length=150, null=True, help_text="User's full name")  # Changed from 'username' to 'name'
    nid_number = models.CharField(max_length=20, unique=True, help_text="National ID number")
    phone = models.CharField(max_length=15, unique=True, help_text="Phone number of the user")
    email = models.EmailField(unique=True, help_text="User's email address")

    class Meta:
        db_table = 'user_profiles'  # Custom table name
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.name

