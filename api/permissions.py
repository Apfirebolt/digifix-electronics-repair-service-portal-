from rest_framework import permissions
from complaints.models import Complaint


class IsTestimonialOwner(permissions.BasePermission):

    # for object level permissions
    def has_object_permission(self, request, view, testimonial_obj):
        return testimonial_obj.written_by.id == request.user.id


class IsAddressOwner(permissions.BasePermission):

    # for object level permissions
    def has_object_permission(self, request, view, address_obj):
        return address_obj.owner.id == request.user.id


class IsComplaintOwner(permissions.BasePermission):

    # for object level permissions
    def has_object_permission(self, request, view, complaint_obj):
        return complaint_obj.created_by.id == request.user.id


class IsThreadOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        obj = Complaint.objects.get(pk=view.kwargs['pk'])
        return obj.created_by == request.user