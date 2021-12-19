from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from . serializers import UserAddressSerializer, UserTestimonialSerializer, CustomUserSerializer, \
    ComplaintSerializer, CommentSerializer
from . permissions import IsTestimonialOwner, IsAddressOwner, IsComplaintOwner
from complaints.models import UserAddress, UserTestimonials, Complaint, Comments, ComplaintImages
from accounts.models import CustomUser


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class ListCustomUsersApiView(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class UserAddressApiView(ListAPIView):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    permission_classes = [IsAuthenticated]


class UserAddressCreateApiView(CreateAPIView):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(owner_id=request.user.id)


class UserAddressUpdateApiView(UpdateAPIView):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    permission_classes = [IsAuthenticated, IsAddressOwner]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        request = serializer.context['request']
        serializer.save(owner_id=request.user.id)


class UserAddressDestroyApiView(DestroyAPIView):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    permission_classes = [IsAuthenticated, IsAddressOwner]
    lookup_field = 'pk'


class UserTestimonialApiView(ListAPIView):
    serializer_class = UserTestimonialSerializer
    queryset = UserTestimonials.objects.all()


class UserTestimonialCreateApiView(CreateAPIView):
    serializer_class = UserTestimonialSerializer
    queryset = UserTestimonials.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(written_by_id=request.user.id)


class UserTestimonialUpdateApiView(UpdateAPIView):
    serializer_class = UserTestimonialSerializer
    queryset = UserTestimonials.objects.all()
    permission_classes = [IsAuthenticated, IsTestimonialOwner]
    lookup_field = 'pk'

    # def perform_update(self, serializer):
    #     request = serializer.context['request']
    #     serializer.save(written_by_id=request.user.id)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Testimonial updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class UserTestimonialDestroyApiView(DestroyAPIView):
    serializer_class = UserTestimonialSerializer
    queryset = UserTestimonials.objects.all()
    permission_classes = [IsAuthenticated, IsTestimonialOwner]
    lookup_field = 'pk'


class ComplaintListApiView(ListAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()


class ComplaintCreateApiView(CreateAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(created_by_id=request.user.id)


class ComplaintUpdateApiView(UpdateAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
    permission_classes = [IsAuthenticated, IsComplaintOwner]


class AddCommentApiView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(written_by_id=request.user.id)


class UpdateCommentApiView(UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated, IsTestimonialOwner]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['commentId'])
        return obj


class DestroyCommentApiView(DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated, IsTestimonialOwner]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['commentId'])
        return obj


class ListCommentApiView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()


