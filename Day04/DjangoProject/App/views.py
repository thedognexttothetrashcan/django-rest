from django.shortcuts import render
from django.views.generic import ListView, DetailView

from App.models import Book


class HelloListView(ListView):

    template_name = 'hello_list.html'

    queryset = Book.objects.all()


class BookDetailView(DetailView):

    template_name = 'book_detail.html'

    queryset = Book.objects.all()
