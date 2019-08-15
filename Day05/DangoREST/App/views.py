import uuid

from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from App.models import User, Blog
from App.serializers import UserSerializer, BlogSerializer


class UsersAPIView(CreateAPIView):

    serializer_class = UserSerializer

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        action = request.query_params.get("action")

        if action == "register":
            return self.create(request, *args, **kwargs)
        elif action == "login":
            u_name = request.data.get("u_name")
            u_password = request.data.get("u_password")

            users = User.objects.filter(u_name=u_name)

            if not users.exists():
                raise APIException(detail="用户不存在", code=status.HTTP_400_BAD_REQUEST)
            user = users.first()

            if not user.check_password(u_password):
                raise APIException(detail="密码错误", code=status.HTTP_400_BAD_REQUEST)

            token = uuid.uuid4().hex

            print(type(cache))

            cache.set(token, user.id, 60*60*24)

            data = {
                "msg": "ok",
                "status": status.HTTP_200_OK,
                "token": token
            }

            return Response(data)
        else:
            raise APIException(detail="请提供正确的action", code=status.HTTP_400_BAD_REQUEST)


class BlogsAPIView(ListCreateAPIView):

    serializer_class = BlogSerializer

    queryset = Blog.objects.all()

    def get_user(self):

        try:

            token = self.request.query_params.get("token")

            user_id = cache.get(token)

            user = User.objects.get(pk=user_id)
        except Exception as e:
            print(e)
            raise APIException(detail="用户信息不存在", code=status.HTTP_404_NOT_FOUND)
        return user

    def get(self, request, *args, **kwargs):

        user = self.get_user()

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        user = self.get_user()

        return self.create(request, *args, **kwargs)
