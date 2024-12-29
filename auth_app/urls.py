from django.urls import path
from auth_app.views import register_user, login_user, protected_view

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('protected_view/', protected_view, name='protected_view'),
    
]
