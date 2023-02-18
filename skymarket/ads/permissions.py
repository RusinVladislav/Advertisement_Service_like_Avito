from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не автор'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
