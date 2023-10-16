from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsCommentOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            # Разрешение на создание комментария для зарегистрированных пользователей
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'destroy']:
            # Разрешение на изменение и удаление комментария только владельцу
            return obj.event.owner == request.user
        return True
