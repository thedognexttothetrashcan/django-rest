from rest_framework.permissions import BasePermission

from AuthenticationAndPermission.models import User


class LoginPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            if isinstance(user, User):
                return True
        except Exception as e:
            print(e)
            return False
