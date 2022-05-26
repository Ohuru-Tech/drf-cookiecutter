from django.conf import settings
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

description_path = getattr(settings, "API_DESCRIPTION_PATH")
with open(description_path, "r") as description_file:
    description = description_file.read()

tos_url = "https://docs.github.com/en/site-policy/github-terms/github-terms-of-service"
license_url = "https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt"
logo_url = "https://image.shutterstock.com/image-vector/no-image-vector-symbol-missing-260nw-1310632172.jpg"
schema_view = get_schema_view(
    openapi.Info(
        title="{{ cookiecutter.project_name }} API",
        default_version="v1",
        description=description,
        contact=openapi.Contact(email=settings.CONTACT_EMAIL),
        license=openapi.License(name="MIT License", url=license_url),
        terms_of_service=tos_url,
        x_logo={"url": logo_url, "backgroundColor": "#fafafa"},
    ),
    public=True,
    permission_classes=(AllowAny,),
)

cache_timeout = 0 if settings.DEBUG else 15

swagger_urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=None),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=cache_timeout),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=cache_timeout),
        name="schema-redoc",
    ),
]
