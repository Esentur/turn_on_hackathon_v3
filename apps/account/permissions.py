from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS

User = get_user_model()


class CustomPermission(BasePermission):
    # create(POST) list(GET) (где не нужен id)
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

        # update delete retrieve (где нужен id)

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and str(request.user) == str(obj.email)
