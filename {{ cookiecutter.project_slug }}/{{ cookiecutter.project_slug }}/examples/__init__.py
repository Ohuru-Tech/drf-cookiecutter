from {{ cookiecutter.project_slug }}.examples.auth_requests import (
    user_login_curl,
    user_logout_curl,
    user_password_reset_confirm_curl,
    user_password_reset_curl,
    user_password_set_curl,
    user_register_curl,
)
from {{ cookiecutter.project_slug }}.examples.auth_responses import (
    user_login_200_example,
    user_login_400_example,
    user_logout_200_example,
    user_logout_401_example,
    user_password_reset_200_example,
    user_password_reset_400_example,
    user_password_reset_confirm_200_example,
    user_password_reset_confirm_400_example,
    user_password_set_200_example,
    user_password_set_401_example,
    user_registration_201_example,
    user_registration_400_example,
)
from {{ cookiecutter.project_slug }}.examples.user_requests import profile_update_curl
from {{ cookiecutter.project_slug }}.examples.user_responses import (
    profile_update_200_example,
    profile_update_401_example,
    profile_update_403_example,
)
