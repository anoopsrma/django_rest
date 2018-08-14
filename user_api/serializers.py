from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Role

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError
    )

User = get_user_model()


class UserSignupSerializer(ModelSerializer):
    email = EmailField(label="Email Address")

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {
           "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user_obj.set_password(password)
        user_obj.save()
        role = Role.objects.filter(name='reader').first()
        if not role:
            raise ValidationError("Something went wrong")
        role.users.add(user_obj)
        return validated_data


class AuthorSignupSerializer(ModelSerializer):
    email = EmailField(label="Email Address")

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {
           "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user_obj.set_password(password)
        user_obj.save()
        role = Role.objects.filter(name='author').first()
        if not role:
            raise ValidationError("Something went wrong")
        role.users.add(user_obj)
        return validated_data


class UserLoginSerializer(ModelSerializer):
    username = CharField(allow_blank=True, required=False, label="Username")
    email = EmailField(allow_blank=True, required=False, label="Email Address")
    token = CharField(allow_blank=True, read_only=True)
    role = CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'role',
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {
           "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get("password")

        if not email and not username:
            raise ValidationError("Username or Email is required to login")

        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Username/Email does not exist")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Invalid Credentials")
        data = {
            "first_name": user_obj.first_name,
            "last_name": user_obj.last_name,
            "username": user_obj.username,
            "email": user_obj.email,
            "role": user_obj.role_set.first(),
            "token": "asdkjsjdkadka"
        }
        return data
