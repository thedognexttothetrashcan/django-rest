from rest_framework import serializers

from ViewSetLearn.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "b_name")