from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth import logout
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, EmptySerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(GenericAPIView):
    serializer_class = EmptySerializer

    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logged out."})