# authenticate/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
