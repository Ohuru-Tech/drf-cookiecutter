from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsProfileOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id
