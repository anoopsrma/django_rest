from django.contrib.auth import get_user_model
from django.db.models import Q
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
    username = CharField(allow_blank=True, required=False, label="Username")
    email = EmailField(allow_blank=True, required=False, label="Email Address")
    token = CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
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
        password = data["password"]

        if not email and not username:
            raise ValidationError("Username or Email is required to login")

        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()
        print(user.first())
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Username/Email does not exist")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Invalid Credentials")
        data["token"] = "klhaldasd;lsadsad;a"
        return data
