from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import UserSignupSerializer


User = get_user_model()


# Create your views here.
class UserSignupView(CreateAPIView):
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
