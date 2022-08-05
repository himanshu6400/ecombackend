from django.urls import path, include
from core.views import UserRegistrationView, LoginView, UserProfileView,UserProfileDataView,ProductView,EditProfileView
from django.contrib import admin
from core import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

#Creating Router Object
router = DefaultRouter()

#Register View Set with Router
# router.register('user', views.UserViewSet, basename='User')
# router.register('profile', views.UserProfileModelViewSet, basename='Profile')


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('login/',LoginView.as_view(), name = 'login' ),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profiledata/', UserProfileDataView.as_view(), name='profiledata'),
    path('productdata/', ProductView.as_view(), name='productdata'),
    path('editprofile/', EditProfileView.as_view(), name='productdata'),
    
    # path('profiledata/', include(router.urls)),
] 