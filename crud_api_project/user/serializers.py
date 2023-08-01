
# The Serializers are responsible for converting model instances to JSON. 
# The serializers also provide deserialization, allowing parsed data to be converted back into complex types,
# after first validating the incoming data.

# This will help the frontend to work with the received data easily. 
# JSON is the standard for data interchange on the web.

from typing import Any
from rest_framework import serializers
from rest_framework.fields import empty
from .models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get('username')
        if username == "":
            raise serializers.ValidationError("Username is required")
        password = data.get('password')
        if password == "":
            raise serializers.ValidationError("Password is required")
        self.validate_username(username)
        self.validate_password(password)
        return data

    
    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username does not match. Please try again")
        return value
    
    def validate_password(self, value):
        if not User.objects.filter(password=value).exists():
            raise serializers.ValidationError("Password does not match. Please try again")
        return value
    


        
   
   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password' ,'is_staff','created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def validateUpdate(self, attrs):
        self.validate_username(attrs['username'])
        self.validate_email(attrs['email'])
        self.validate_password(attrs['password'])
        self.validate_username_password(attrs)
    
    def validate(self, attrs):
        self.validate_username(attrs['username'])
        self.validate_email(attrs['email'])
        self.validate_password(attrs['password'])
        self.validate_username_password(attrs)
        return attrs


    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists. Please try with another username")
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.Please try with another email")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")
        return value
    
    
    def validate_username_password(self, data):
        if data['username'] == data['password']:
            raise serializers.ValidationError("Username and Password must be different")
        return data