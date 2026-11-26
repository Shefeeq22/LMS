from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

    def has_permission(self, request, view):
        
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if hasattr(obj,"trainer"):

            return obj.trainer == request.user

        elif hasattr(obj,"course"):

            return obj.course.trainer == request.user

        elif hasattr(obj,"module"):

            return obj.module.course.trainer == request.user

        return False