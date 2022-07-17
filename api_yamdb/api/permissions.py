from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or (
                request.user.is_authenticated
                and (request.user.role == 'admin')
            )
            or (
                request.user.is_authenticated
                and (request.user.role == 'moderator')
            )
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and (request.user.role == 'admin')
                    )
                )


class IsAdminOrMe(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_staff
            or (request.user.is_authenticated and request.user.role == 'admin')
            or (view.name == 'Me' and request.user.is_authenticated)
        )
