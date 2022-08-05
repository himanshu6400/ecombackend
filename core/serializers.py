from django.forms import ValidationError
from rest_framework import serializers
from core.models import User, Profile
from .models import Product

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields =['email','name','mobile', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only':True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password does not match')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSeriaizer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model= User 
        fields = ['id', 'name' , 'email','mobile',]

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model= Profile 
        fields = ['user','gender' , 'locality','city','address','pin','state','profile_image']

class ProductSerializer(serializers.ModelSerializer):     
    class Meta: 
        model= Product 
        fields = ['product_image',]

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = ['gender','locality','city','address','pin','state','profile_image',]