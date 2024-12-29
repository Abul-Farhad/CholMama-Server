from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount, UserProfile

# Register UserAccount with custom UserAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_app.models import UserAccount

@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    # Override fieldsets to exclude 'groups' and 'user_permissions'
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone'),
        }),
    )
    # Override to exclude problematic fields
    list_display = ('email', 'phone')
    ordering = ('email',)
    filter_horizontal = ()  # Remove 'groups' and 'user_permissions'
    list_filter = ()  # Remove 'is_staff', 'is_superuser', 'is_active', 'groups'

# Register UserProfile with default ModelAdmin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nid_number', 'phone')  # Fields to display
    search_fields = ('username', 'email', 'nid_number', 'phone')  # Enable searching
