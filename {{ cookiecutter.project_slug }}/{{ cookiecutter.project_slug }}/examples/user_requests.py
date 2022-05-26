from django.conf import settings

token = getattr(settings, "SAMPLE_AUTH_TOKEN")
origin = getattr(settings, "HOSTED_DOMAIN")
auth = f'-H "Authorization: Bearer {token}"' if token else ""

profile_update_body = {"profile_pic": "some_pic.jpg"}

profile_update_curl = f"""
# Update the profile pic of a user
curl \\
  -X POST \\
  -H "Content-Type: application/json" \\
  {auth} \\
  -d '{profile_update_body}' \\
  "{origin}/v1/"
"""  # noqa
