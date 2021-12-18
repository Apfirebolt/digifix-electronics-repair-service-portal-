from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from . serializers import UserAddressSerializer, UserTestimonialSerializer
from complaints.models import UserAddress, UserTestimonials


class UserAddressApiView(ListAPIView):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()


class UserTestimonialApiView(ListAPIView):
    serializer_class = UserTestimonialSerializer
    queryset = UserTestimonials.objects.all()

