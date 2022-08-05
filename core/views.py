import json
from unicodedata import category
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from core.serializers import UserRegistrationSerializer, LoginSeriaizer, UserProfileSerializer,ProfileSerializer, ProductSerializer,EditProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from core.renderer import UserRenderer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import User, Profile, Product, OrderPlaced, Cart, Customer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer


#Generate Token Manually #copied from simple-jwt 
def get_tokens_for_user(user): 
    refresh = RefreshToken.for_user(user) 
    return { 
        'refresh': str(refresh), 
        'access': str(refresh.access_token), 
    } 

# Create your views here.

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format= None):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response ({'token':token, 'msg':'User Registration Successfull'},status=status.HTTP_201_CREATED )

class LoginView(APIView):
    renderer_classes =[UserRenderer]
    def post(self, request, format=None):
        serializer = LoginSeriaizer(data = request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email =email, password = password)
        if user is not None: 
            token = get_tokens_for_user(user) 
            return Response({'token':token ,'msg':'Login Success'}, status = status.HTTP_200_OK) 
        else: 
            return Response({'errors':{'non_field_errors':['Email or password is not valid']}}, status = status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView): 
    renderer_classes = [UserRenderer] 
    permission_classes = [IsAuthenticated] 
    
    def get(self, request, format=None): 
        serializer = UserProfileSerializer(request.user) 
        return Response(serializer.data, status=status.HTTP_200_OK)


#using API View
class UserProfileDataView(APIView):
    renderer_classes = [UserRenderer] 
    permission_classes = [IsAuthenticated] 
    def get(self, request, format=None):
        # user = Profile.objects.all()
        serializer = ProfileSerializer(request.user.profile, context={'request': request})
        # return Response(serializer.data, status=status.HTTP_200_OK)
        # user = Profile.objects.filter(user = request.user)
        # serializer = ProfileSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class ProductView(APIView):
#     renderer_classes = [UserRenderer]
#     def get(self, request, format=None):
#         Jeans = Product.objects.get(id=14)
#         serializer = ProductSerializer(Jeans, context={"request": request}  )  
#         return Response(serializer.data ,status=status.HTTP_200_OK)

class ProductView(APIView):
    renderer_classes = [UserRenderer]
    def get(self, request, format=None):
        Jeans = Product.objects.filter(category='Jeans')
        serializer = ProductSerializer(Jeans, many=True, context={"request": request})  
        return Response(serializer.data ,status=status.HTTP_200_OK)

class EditProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated] 
    def get(self, request, format=None):
        serializer = EditProfileSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Profile Updated Successfull'}, status = status.HTTP_200_OK)



