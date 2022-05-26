from {{ cookiecutter.project_slug }}.apps.accounts.views.auth_views import (
    UserLoginView,
    UserLogoutView,
    UserPasswordResetConfirmView,
    UserPasswordResetView,
    UserPasswordSetView,
    UserRegistrationView,
    VerifyEmailRegisterView,
)
from {{ cookiecutter.project_slug }}.apps.accounts.views.user_views import ProfileViewSet
