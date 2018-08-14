from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    ValidationError
    )

User = get_user_model()


class UserSignupSerializer(ModelSerializer):
    email2 = EmailField(label="Confirm Email")
    email = EmailField(label="Confirm Address")


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email2',
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
                username = username,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    username = CharField(label="Username")
    email = EmailField(label="Confirm Address")
    token = CharField(allow_blank=True, read_only=True)


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {
           "password": {
                "write_only": True
            }
        }
