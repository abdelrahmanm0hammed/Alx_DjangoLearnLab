from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only =True,
        min_length = 8 )
    class Meta:
        model = User
        fields= ['username', 'password','email']
    def create(self, validated_data):     
        user=User.objects.create_user(username= validated_data['username'], password= validated_data['password'],email= validated_data.get('email'))
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'],
                            password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data['user']= user
        return data
    