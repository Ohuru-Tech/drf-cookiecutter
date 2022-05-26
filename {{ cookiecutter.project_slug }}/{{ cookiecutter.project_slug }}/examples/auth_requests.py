from django.conf import settings

token = getattr(settings, "SAMPLE_AUTH_TOKEN")
origin = getattr(settings, "HOSTED_DOMAIN")
auth = f'-H "Authorization: Bearer {token}"' if token else ""


user_register_curl = f"""
# Update the profile pic of a user
curl \\
  -X POST \\
  -H "Content-Type: application/json" \\
  -d '{{ '{{' }} 
      "name": "Jon Doe", \\
      "email": "jondoe@customer.com", \\
      "password1": "some_password", \\
      "password2": "some_password", \\
      "account_type": "general"
    {{ '}}' }} \\
  "{origin}/v1/"
"""  # noqa

user_login_curl = f"""
# User login endpoint
curl \\
  -X POST \\
  -H  "accept: application/json" \\
  -d '{{ '{{' }} 
    "email": "user@wew.com", \\
    "password": "password1234" \\
  {{ '}}' }} \\'
  "{origin}/v1/"
"""  # noqa

user_logout_curl = f"""
# User Logout endpoint
curl \\
  -X POST \\
  -H "Content-Type: application/json" \\
  {auth} \\
  -d '{{ '{{' }}"profile_pic": "some_pic.jpg"{{ '}}' }} \\
  "{origin}/v1/"
"""  # noqa

user_password_reset_curl = f"""
# User password endpoint
curl \\
  -X POST \\
  -H "Content-Type: application/json" \\
  -d '{{ '{{' }}"email": "user@example.com"{{ '}}' }} \\
  "{origin}/v1"
"""  # noqa

user_password_reset_confirm_curl = f"""
# User password reset confirm endpoint
curl \\
  -X POST \\
  -H "Content-Type: application/json" \\
  -d '{{ '{{' }}
    "new_password1": "dfkjsdlfsdf", \\
    "new_password2": "dfkjsdlfsdf", \\
    "token": "3434khj234-3432423", \\
    "uid": "1"
  {{ '}}' }} \\
  "{origin}/v1"
"""  # noqa

user_password_set_curl = f"""
# User password set endpoint
curl \\
  -X POST \\
  -H "Content-Type: application/json" \\
  {auth} \\
  -d '{{ '{{' }}
    "old_password": "dsdsds", \\
    "new_password1": "dfkjsdlfsdf", \\
    "new_password2": "dfkjsdlfsdf", \\
  {{ '}}' }} \\
  "{origin}/v1"
"""  # noqa
