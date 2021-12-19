from rest_framework import serializers
from complaints.models import UserAddress, UserTestimonials, Complaint, Comments, ComplaintImages
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_customer', 'is_staff', 'is_engineer', 'password')

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = '__all__'
        read_only_fields = ['created_by']


class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = ['id', 'address', 'is_primary', 'owner']
        read_only_fields = ['owner']


class UserTestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTestimonials
        fields = ['id', 'written_by', 'content', 'posted_at', 'service_rating']
        read_only_fields = ['written_by', 'posted_at']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['written_by']