import uuid

from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from AuthenticationAndPermission.auth import UserAuthentication
from AuthenticationAndPermission.models import User, Blog, Address
from AuthenticationAndPermission.permissions import LoginPermission
from AuthenticationAndPermission.serializers import UserSerializer, BlogSerializer, AddressSerializer
from AuthenticationAndPermission.throttling import BlogThrottling


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
    authentication_classes = (UserAuthentication,)
    permission_classes = (LoginPermission, )
    throttle_classes = (BlogThrottling,)

    def perform_create(self, serializer):
        serializer.save(b_author=self.request.user)

    def get_queryset(self):
        # return self.queryset.filter(b_author=self.request.user)
        query_set = super().get_queryset()
        return query_set.filter(b_author=self.request.user)


class AddressesAPIView(ListCreateAPIView):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    authentication_classes = (UserAuthentication,)
    permission_classes = (LoginPermission,)


    # def get(self, request, *args, **kwargs):
    #     print(request.auth)
    #
    #     if not request.auth:
    #         raise APIException(detail="not auth")
    #
    #     return self.list(request, *args, **kwargs)