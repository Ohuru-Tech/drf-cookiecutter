from allauth.account.views import ConfirmEmailView as AllauthConfirmEmailView
from django.http import HttpResponse
from django.urls import path, re_path

from {{ cookiecutter.project_slug }}.apps.accounts.views import (
    ResendVerifyEmailView,
    UserLoginView,
    UserLogoutView,
    UserPasswordResetConfirmView,
    UserPasswordResetView,
    UserPasswordSetView,
    UserRegistrationView,
    VerifyEmailRegisterView,
)


# The following function is to be used with the password_reset_confirm URL.
# Scroll down for more details.
def empty_view(request):
    return HttpResponse("")


rest_auth_urls = [
    # Rest Auth Registration Endpoints
    path(
        "accounts/registration/",
        UserRegistrationView.as_view(),
        name="rest_register",
    ),
    path(
        "accounts/registration/verify-email/",
        VerifyEmailRegisterView.as_view(),
        name="rest_verify_email",
    ),
    path(
        "accounts/registration/account-confirm-email/",
        VerifyEmailRegisterView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "accounts/registration/account-resend-confirmation-mail/",
        ResendVerifyEmailView.as_view(),
        name="account_email_verification_resend",
    ),
    re_path(
        r"^accounts/registration/account-confirm-email/(?P<key>[-:\w]+)/$",  # NOQA
        AllauthConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    path(
        "accounts/login/",
        UserLoginView.as_view(),
        name="rest_login",
    ),
    path(
        "accounts/logout/",
        UserLogoutView.as_view(),
        name="rest_logout",
    ),
    path(
        "accounts/password/reset/",
        UserPasswordResetView.as_view(),
        name="rest_password_reset",
    ),
    path(
        "accounts/password/reset/confirm/",
        UserPasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path(
        "accounts/password/change/",
        UserPasswordSetView.as_view(),
        name="rest_password_change",
    ),
]
