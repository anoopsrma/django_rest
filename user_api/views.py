from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import UserSignupSerializer, UserLoginSerializer


User = get_user_model()


class UserSignupView(CreateAPIView):
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, HTTP_200_OK)
    queryset = User.objects.all()
