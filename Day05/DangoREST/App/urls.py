from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^users/', views.UsersAPIView.as_view()),
    url(r'^blogs/', views.BlogsAPIView.as_view()),
]