from drf_yasg import openapi

from {{ cookiecutter.project_slug }}.apps.accounts.serializers import (
    CustomLoginSerializer,
    CustomPasswordChangeSerializer,
    CustomPasswordResetConfirmSerializer,
    CustomPasswordResetSerializer,
    CustomRegisterSerializer,
    CustomTokenSerializer,
)
from {{ cookiecutter.project_slug }}.docs.docs_utils import fields_to_md
from {{ cookiecutter.project_slug }}.examples import (
    user_login_200_example,
    user_login_400_example,
    user_login_curl,
    user_logout_200_example,
    user_logout_401_example,
    user_logout_curl,
    user_password_reset_200_example,
    user_password_reset_400_example,
    user_password_reset_confirm_200_example,
    user_password_reset_confirm_400_example,
    user_password_reset_confirm_curl,
    user_password_reset_curl,
    user_password_set_200_example,
    user_password_set_401_example,
    user_password_set_curl,
    user_register_curl,
    user_registration_201_example,
    user_registration_400_example,
)


class AuthRegister:
    desc = f"""
User Registration is an API endpoint to allow users to
register to the website.

By using this endpoint you make a POST call to register a user by
providing his {fields_to_md(CustomRegisterSerializer.field_names)}, the
{fields_to_md(CustomRegisterSerializer.password_fields)} fields need to be same
    """  # noqa

    responses = {
        "201": openapi.Response(
            description="Created",
            examples=user_registration_201_example,
            schema=CustomTokenSerializer,
        ),
        "400": openapi.Response(
            description="Error: Bad Request",
            examples=user_registration_400_example,
        ),
    }

    code_examples = [{"lang": "Bash", "source": user_register_curl}]

    swagger_setup = {
        "operation_id": "User Registration",
        "operation_description": desc,
        "request_body": CustomRegisterSerializer,
        "responses": responses,
        "code_examples": code_examples,
        "security": [],
    }


class AuthLogin:
    desc = f"""
User Login is an API endpoint to allow users to
login to the website. After succesful authentication, the caller
is provided with a temporary token, using which the client can make
authenticated requests to the server, this token will also be responsible
in managing authorization i.e., different kinds of users will be able to
login and perform allowed actions which are decided based on the kind
of account they have with the server.

The endpoint accepts a POST request with
{fields_to_md(CustomLoginSerializer.field_names)}
and returns a token with user details after the credentials are verified by
the server
    """
    responses = {
        "200": openapi.Response(
            description="OK", examples=user_login_200_example
        ),
        "400": openapi.Response(
            description="Error: Bad Request", examples=user_login_400_example
        ),
    }

    code_examples = [{"lang": "bash", "source": user_login_curl}]

    swagger_setup = {
        "operation_id": "User Login",
        "operation_description": desc,
        "request_body": CustomLoginSerializer,
        "responses": responses,
        "code_examples": code_examples,
        "security": [],
    }


class AuthLogout:
    desc = """
User Logout deletes the token generated for the current user object.
Calling this endpoint will delete the token associated with the current
user from the db. The user is identified with the help of the token
supplied in the Authorization header.
"""
    responses = {
        "200": openapi.Response(
            description="OK", examples=user_logout_200_example
        ),
        "401": openapi.Response(
            description="Unauthorized", examples=user_logout_401_example
        ),
    }

    code_examples = [{"lang": "bash", "source": user_logout_curl}]

    swagger_setup = {
        "operation_id": "User Logout",
        "operation_description": desc,
        "responses": responses,
        "code_examples": code_examples,
    }


class AuthPasswordReset:
    desc = f"""
The Password Reset endpoint is used to generate a link to allow users
to reset their password.
The link generated utilizes the front-end base url you have updated in
the settings and
constructs a link of the following form:
`<your_frontend_url>/<user_id>/<token>`, you are required to parse these
values and make a call
to `Password Reset Confirm` endpoint for updating the password for the user

The endpoint accepts {fields_to_md(CustomPasswordResetSerializer.fields_names)}
"""  # noqa
    responses = {
        "200": openapi.Response(
            description="OK", examples=user_password_reset_200_example
        ),
        "400": openapi.Response(
            description="BAD REQUEST", examples=user_password_reset_400_example
        ),
    }

    code_examples = [{"lang": "bash", "source": user_password_reset_curl}]

    swagger_setup = {
        "operation_id": "Password Reset",
        "operation_description": desc,
        "request": CustomPasswordResetSerializer,
        "responses": responses,
        "code_examples": code_examples,
        "security": [],
    }


class AuthPasswordResetConfirm:
    desc = f"""
The Password Reset Confirm endpoint expects you to pass in the token
you get after the user hits the link he gets in the email after initiating
a reset request. The endpoint accepts
{fields_to_md(CustomPasswordResetConfirmSerializer.field_names)}
"""  # noqa
    responses = {
        "200": openapi.Response(
            description="OK", examples=user_password_reset_confirm_200_example
        ),
        "400": openapi.Response(
            description="BAD REQUEST",
            examples=user_password_reset_confirm_400_example,
        ),
    }

    code_examples = [
        {"lang": "bash", "source": user_password_reset_confirm_curl}
    ]

    swagger_setup = {
        "operation_id": "Password Reset Confirm",
        "operation_description": desc,
        "request_body": CustomPasswordResetConfirmSerializer,
        "responses": responses,
        "code_examples": code_examples,
        "security": [],
    }


class AuthPasswordSet:
    desc = f"""
This endpoint is accesible to authenticated users and is used to set
a new password for a user provided the correct `old_password` is provided.

The endpoint accepts the {fields_to_md(CustomPasswordChangeSerializer.field_names)}.
"""  # noqa
    responses = {
        "200": openapi.Response(
            description="OK", examples=user_password_set_200_example
        ),
        "401": openapi.Response(
            description="UNAUTHORIZED", examples=user_password_set_401_example
        ),
    }

    code_examples = [{"lang": "bash", "source": user_password_set_curl}]

    swagger_setup = {
        "operation_id": "Password Set",
        "operation_description": desc,
        "request_body": CustomPasswordChangeSerializer,
        "responses": responses,
        "code_examples": code_examples,
        "security": [],
    }
