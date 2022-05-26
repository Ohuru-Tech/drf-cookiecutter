from django.utils.decorators import method_decorator
from drf_psq import PsqMixin, Rule
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from {{ cookiecutter.project_slug }}.apps.accounts.models.user_models import User
from {{ cookiecutter.project_slug }}.apps.accounts.serializers.user_serializers import (
    ProfileCreateUpdateSerializer,
    UserInfoSerializer,
)
from {{ cookiecutter.project_slug }}.apps.common.custom_auto_schema import CustomAutoSchema
from {{ cookiecutter.project_slug }}.docs.user_docs import ProfileUpdate


@method_decorator(
    swagger_auto_schema(**ProfileUpdate.swagger_setup), "partial_update"
)
class ProfileViewSet(UpdateModelMixin, PsqMixin, GenericViewSet):
    http_method_names = ["patch"]
    parser_classes = [MultiPartParser]
    swagger_schema = CustomAutoSchema
    permission_classes = [IsAuthenticated]
    psq_rules = {
        "partial_update": [
            Rule([IsAuthenticated], ProfileCreateUpdateSerializer)
        ]
    }

    def get_queryset(self):
        return User.objects.all()

    # override perform_update to associate user
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    # override update to have custom response
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(
            UserInfoSerializer(instance=instance).data,
            status=status.HTTP_200_OK,
        )
