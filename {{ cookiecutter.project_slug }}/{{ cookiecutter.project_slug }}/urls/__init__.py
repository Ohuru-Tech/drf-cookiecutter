from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from {{ cookiecutter.project_slug }}.urls.auth_urls import rest_auth_urls
from {{ cookiecutter.project_slug }}.urls.swagger_urls import swagger_urlpatterns
from {{ cookiecutter.project_slug }}.urls.versioned_urls import versioned_urls

API_PREFIX = getattr(settings, "API_PREFIX")
API_VERSION = getattr(settings, "API_VERSION")
DOCS_PREFIX = getattr(settings, "DOCS_PREFIX")
PLATFORM_PREFIX = getattr(settings, "PLATFORM_PREFIX")

admin_urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    path(f"{API_PREFIX}/{API_VERSION}/", include(rest_auth_urls)),
    path(f"{API_PREFIX}/{API_VERSION}/", include(versioned_urls)),
    path(
        f"{PLATFORM_PREFIX}/{DOCS_PREFIX}/{API_VERSION}/",
        include(swagger_urlpatterns),
    ),
]

urlpatterns += admin_urlpatterns

# enable serve static by django or uwsgi

urlpatterns += static(
    getattr(settings, "STATIC_URL"),
    document_root=getattr(settings, "STATIC_ROOT"),
)

if getattr(settings, "DEBUG"):
    urlpatterns += static(
        getattr(settings, "MEDIA_URL"),
        document_root=getattr(settings, "MEDIA_ROOT"),
    )

# enable debug_toolbar for local develop (if installed)
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
