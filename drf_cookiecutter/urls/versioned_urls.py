from django.urls import include, path
from rest_framework.routers import SimpleRouter

from drf_cookiecutter.apps.accounts.views import ProfileViewSet

router = SimpleRouter()
router.register("profile", ProfileViewSet, basename="profile")

versioned_urls = [path("", include(router.urls))]
