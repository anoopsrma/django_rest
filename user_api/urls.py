from django.contrib import admin
from django.urls import path
from .views import UserSignupView, UserLoginView

urlpatterns = [
    path('api/v1/user/register/', UserSignupView.as_view(), name='register'),
    path('api/v1/user/login/', UserLoginView.as_view(), name='login'),
]
