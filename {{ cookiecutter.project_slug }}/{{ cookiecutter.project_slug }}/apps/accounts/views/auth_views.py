# This is here to override the auth views and have custom docs for them
from allauth.account.views import ConfirmEmailView as AllauthConfirmEmailView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from {{ cookiecutter.project_slug }}.apps.accounts.serializers.user_serializers import (
    CustomPasswordChangeSerializer,
    CustomPasswordResetConfirmSerializer,
)
from {{ cookiecutter.project_slug }}.apps.common.custom_auto_schema import CustomAutoSchema
from {{ cookiecutter.project_slug }}.docs.auth_docs import (
    AuthLogin,
    AuthLogout,
    AuthPasswordReset,
    AuthPasswordResetConfirm,
    AuthPasswordSet,
    AuthRegister,
)


class UserRegistrationView(RegisterView):
    swagger_schema = CustomAutoSchema

    @swagger_auto_schema(**AuthRegister.swagger_setup)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class VerifyEmailRegisterView(VerifyEmailView):
    swagger_schema = None


class ConfirmEmailView(AllauthConfirmEmailView):
    swagger_schema = None


class UserLoginView(LoginView):
    swagger_schema = CustomAutoSchema

    @swagger_auto_schema(**AuthLogin.swagger_setup)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    swagger_schema = CustomAutoSchema
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(**AuthLogout.swagger_setup)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserPasswordResetView(PasswordResetView):
    @swagger_auto_schema(**AuthPasswordReset.swagger_setup)
    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        passed = serializer.save()
        if not passed:
            return Response(
                {"detail": _("No user found with the given email")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Return the success message with OK HTTP status
        return Response(
            {"detail": _("Password reset e-mail has been sent.")},
            status=status.HTTP_200_OK,
        )


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    serializer_class = CustomPasswordResetConfirmSerializer

    @swagger_auto_schema(**AuthPasswordResetConfirm.swagger_setup)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserPasswordSetView(PasswordChangeView):
    serializer_class = CustomPasswordChangeSerializer

    @swagger_auto_schema(**AuthPasswordSet.swagger_setup)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
