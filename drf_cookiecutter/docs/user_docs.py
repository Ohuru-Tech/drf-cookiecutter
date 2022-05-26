from drf_yasg import openapi

from drf_cookiecutter.apps.accounts.serializers.user_serializers import (
    ProfileCreateUpdateSerializer,
    UserInfoSerializer,
)
from drf_cookiecutter.docs.docs_utils import fields_to_md
from drf_cookiecutter.examples import (
    profile_update_200_example,
    profile_update_401_example,
    profile_update_403_example,
    profile_update_curl,
)


class ProfileUpdate:
    desc = f"""
Profile Update is an API endpoint to update the profile associated
with a particular user.

By using this endpoint, you can make a patch call to update the profile
associated with any user. The {fields_to_md(ProfileCreateUpdateSerializer.fields_names)}
are the fields that can currently be updated
    """  # noqa

    responses = {
        "200": openapi.Response(
            description="OK",
            examples=profile_update_200_example,
            schema=UserInfoSerializer,
        ),
        "401": openapi.Response(
            description="Unauthorized", examples=profile_update_401_example
        ),
        "403": openapi.Response(
            description="Permission Denied",
            examples=profile_update_403_example,
        ),
    }

    code_examples = [{"lang": "Bash", "source": profile_update_curl}]

    swagger_setup = {
        "operation_id": "Profile Update",
        "operation_description": desc,
        "request_body": ProfileCreateUpdateSerializer,
        "responses": responses,
        "code_examples": code_examples,
    }
