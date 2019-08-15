from django.conf.urls import url

from AuthenticationAndPermission import views

urlpatterns = [
    url(r'^users/', views.UsersAPIView.as_view()),
    url(r'^blogs/', views.BlogsAPIView.as_view()),
    url(r'^addresses/', views.AddressesAPIView.as_view()),
]