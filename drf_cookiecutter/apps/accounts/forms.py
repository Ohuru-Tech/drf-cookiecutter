from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.forms import default_token_generator
from allauth.account.utils import (
    filter_users_by_email,
    user_pk_to_url_str,
    user_username,
)
from dj_rest_auth.forms import AllAuthPasswordResetForm
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


# Customize the password reset link and email
class CustomPasswordResetForm(AllAuthPasswordResetForm):
    def clean_email(self):
        """
        Invalid email should not raise error, as this would leak users
        for unit test: test_password_reset_with_invalid_email
        """
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        self.users = filter_users_by_email(email, is_active=True)
        return self.cleaned_data["email"]

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]
        token_generator = kwargs.get(
            "token_generator", default_token_generator
        )

        # Do not send an email if we do not get any matching users
        if not self.users:
            return

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # send the password reset email
            url = (
                f"{getattr(settings, 'PASSWORD_RESET_URL')}"
                + f"{user_pk_to_url_str(user)}/{temp_key}"
            )

            context = {
                "current_site": current_site,
                "user": user,
                "password_reset_url": url,
                "request": request,
            }
            if (
                app_settings.AUTHENTICATION_METHOD
                != app_settings.AuthenticationMethod.EMAIL
            ):
                context["username"] = user_username(user)
            get_adapter(request).send_mail(
                "account/email/password_reset_key", email, context
            )
        return self.cleaned_data["email"]
