from rest_framework import permissions


class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_staff


class IsLibrarianOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsOwnerOrLibrarian(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.member.user == request.user
