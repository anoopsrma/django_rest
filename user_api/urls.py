from django.contrib import admin
from django.urls import path
from .views import UserSignupView, UserLoginView

urlpatterns = [
    path('api/v1/register/', UserSignupView.as_view(), name='register'),
    path('api/v1/login/', UserLoginView.as_view(), name='login'),
]
