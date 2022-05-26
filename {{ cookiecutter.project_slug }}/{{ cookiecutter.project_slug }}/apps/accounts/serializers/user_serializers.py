from dj_rest_auth.models import TokenModel
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import (
    LoginSerializer,
    PasswordChangeSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    TokenSerializer,
)
from django.conf import settings
from rest_framework import serializers

from {{ cookiecutter.project_slug }}.apps.accounts.forms import CustomPasswordResetForm
from {{ cookiecutter.project_slug }}.apps.accounts.models.user_models import AccountType, User


class CustomLoginSerializer(LoginSerializer):
    field_names = ["email", "password"]
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"})

    def update(self, instance, validated_data):
        return super(CustomLoginSerializer, self).update(
            instance, validated_data
        )

    def create(self, validated_data):
        return super(CustomLoginSerializer, self).create(validated_data)


class CustomRegisterSerializer(RegisterSerializer):
    field_names = [
        "username",
        "name",
        "password1",
        "password2",
        "account_type",
    ]
    password_fields = ["password1", "password2"]

    username = None
    name = serializers.CharField(max_length=255, required=True)
    account_type = serializers.ChoiceField(
        choices=AccountType.choices, default=AccountType.GENERAL
    )

    def get_cleaned_data(self):
        return {
            "password1": self._validated_data.get("password1", ""),
            "email": self._validated_data.get("email", ""),
            "name": self._validated_data.get("name", ""),
            "account_type": self._validated_data.get(
                "account_type", "general"
            ),
        }

    def custom_signup(self, request, user):
        cleaned_data = self.get_cleaned_data()
        user.name = cleaned_data.get("name")
        user.account_type = cleaned_data.get("account_type")
        user.save()

    def update(self, instance, validated_data):
        return super(CustomRegisterSerializer, self).update(
            instance, validated_data
        )

    def create(self, validated_data):
        return super(CustomRegisterSerializer, self).create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "account_type",
            "profile_pic",
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = ("key", "user")


class ProfileCreateUpdateSerializer(serializers.ModelSerializer):
    fields_names = ["name", "profile_pic"]

    class Meta:
        model = User
        fields = ("profile_pic", "name")


class UserInfoSerializer(serializers.ModelSerializer):
    fields_names = ["id", "name", "profile_pic"]

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "profile_pic",
        )


# Override the Password Serializer to customize password reset url
class CustomPasswordResetSerializer(PasswordResetSerializer):
    fields_names = ["email"]

    # Override to use custom form
    @property
    def password_reset_form_class(self):
        return CustomPasswordResetForm

    def save(self):
        from allauth.account.forms import default_token_generator

        request = self.context.get("request")
        # Set some values to trigger the send_email method.
        opts = {
            "use_https": request.is_secure(),
            "from_email": getattr(settings, "DEFAULT_FROM_EMAIL"),
            "request": request,
            "token_generator": default_token_generator,
        }

        opts.update(self.get_email_options())
        return self.reset_form.save(**opts)


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    field_names = ["new_password1", "new_password2", "uid", "token"]


class CustomPasswordChangeSerializer(PasswordChangeSerializer):
    field_names = ["old_password", "new_password1", "new_password2"]
