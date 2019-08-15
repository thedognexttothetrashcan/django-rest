from django.conf.urls import url

from SerializerLearn import views

urlpatterns = [
    url(r'^animals/$', views.animals),
    url(r'^animals/(?P<pk>\d+)/', views.animal),
    url(r'^spiders/', views.spiders),
    url(r'^peoples/', views.PeopleAPIView.as_view()),
    url(r'^haha/', views.HelloAPIView),
]