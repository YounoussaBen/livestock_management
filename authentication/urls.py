# project/urls.py
from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    # Add other app's URLs here as well
]
