from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . serializers import UserAddressSerializer, UserTestimonialSerializer, CustomUserSerializer, ComplaintSerializer
from . permissions import IsTestimonialOwner
from complaints.models import UserAddress, UserTestimonials, Complaint
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