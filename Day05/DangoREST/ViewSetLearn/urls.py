from django.conf.urls import url

from ViewSetLearn import views

# 创建书，  获取所有书， 获取单本书
urlpatterns = [
    url(r'^books/$', views.BookViewSet.as_view(
        {
            "get": "list",
            "post": "create",
        }
    )),
    url(r'^books/(?P<pk>\d+)/', views.BookViewSet.as_view(
        {
            "get": "retrieve",
        }
    )),
]