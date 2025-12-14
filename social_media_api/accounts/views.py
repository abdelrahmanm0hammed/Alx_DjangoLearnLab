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

class followUserView(generics.GenericAPIView):
    serializer_class= UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow= User.objects.get(id= user_id)
        request.user.following.add(user_to_follow)
        request.user.save()
        return Response({'status':'followed', 'user': UserSerializer(user_to_follow).data})
    
class UnfollowUserView(generics.GenericAPIView):
    serializer_class= UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow= User.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        request.user.save()
        return Response({'status':'unfollowed', 'user': UserSerializer(user_to_unfollow).data})