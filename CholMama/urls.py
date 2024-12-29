
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.views.generic.base import RedirectView

def welcome(request):
    return HttpResponse("<h1>Welcome to CholMama!</h1><p>This is the root URL.</p>")

urlpatterns = [
    path('', welcome),  # Redirect to the registration page
    # path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),  # Include the URLs from auth_app
]
