from django.conf.urls import url

from ViewLearn import views

urlpatterns = [
    url(r'^computers/$', views.ComputersAPIView.as_view()),
    url(r'^computers/(?P<pk>\d+)/', views.ComputerAPIView.as_view()),
]