from rest_framework import viewsets

from ViewSetLearn.models import Book
from ViewSetLearn.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()