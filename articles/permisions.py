from rest_framework.permissions import \
    BasePermission, \
    SAFE_METHODS


class IsOwnerOrStaffOrReadOnly(BasePermission):
    """
    My permission for owners comments
    """

    def has_object_permission(self,request,view,obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (obj.user == request.user or request.user.is_staff)
        )