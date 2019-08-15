from rest_framework import routers

from App.views import UserViewSet, GroupViewSet, BookViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("books", BookViewSet)