from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class= RegisterSerializer
    permission_classes=[permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes= [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.vaidated_data['user']
        token, _=Token.objects.get_or_create(user=user)
        
        return Response({
            'token':token.key,
            'user':UserSerializer(user).data
        })
        

class ProfileView(generics.RetrieveAPIView):
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

