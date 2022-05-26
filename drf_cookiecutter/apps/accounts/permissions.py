from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    message = "The account is not of the authenticated user"

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
