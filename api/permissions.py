from rest_framework import permissions


class IsTestimonialOwner(permissions.BasePermission):

    # for object level permissions
    def has_object_permission(self, request, view, testimonial_obj):
        return testimonial_obj.written_by.id == request.user.id