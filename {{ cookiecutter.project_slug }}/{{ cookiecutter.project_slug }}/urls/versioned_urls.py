from django.urls import include, path
from rest_framework.routers import SimpleRouter

from {{ cookiecutter.project_slug }}.apps.accounts.views import ProfileViewSet
from {{ cookiecutter.project_slug }}.apps.{{ cookiecutter.app_name }}.views import ItemViewSet

router = SimpleRouter()
router.register("profile", ProfileViewSet, basename="profile")
router.register("items", ItemViewSet, basename="items")

versioned_urls = [path("", include(router.urls))]
