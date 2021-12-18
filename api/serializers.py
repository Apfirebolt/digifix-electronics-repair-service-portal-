from rest_framework import serializers
from complaints.models import UserAddress, UserTestimonials


class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = ['address', 'owner', 'is_primary']


class UserTestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTestimonials
        fields = ['written_by', 'content']