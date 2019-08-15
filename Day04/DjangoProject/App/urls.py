from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.HelloListView.as_view()),
    url(r"^books/(?P<pk>\d+)", views.BookDetailView.as_view(), name='book_detail'),
]