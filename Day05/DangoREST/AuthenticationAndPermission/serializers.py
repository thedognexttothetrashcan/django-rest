from rest_framework import serializers

from AuthenticationAndPermission.models import User, Blog, Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "u_name", "u_password")


class BlogSerializer(serializers.ModelSerializer):

    b_author = serializers.ReadOnlyField(source="b_author.u_name")

    class Meta:
        model = Blog
        fields = ("id", "b_title", "b_content", "b_author")


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "a_address")