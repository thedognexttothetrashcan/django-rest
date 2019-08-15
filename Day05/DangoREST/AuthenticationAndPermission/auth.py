from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from AuthenticationAndPermission.models import User


class UserAuthentication(BaseAuthentication):
    # 认证方法   认证成功会返回一个元组， 元组中包含两个元素，一个是用户，另外一个是令牌
    def authenticate(self, request):

        try:

            token = request.query_params.get("token")

            user_id = cache.get(token)

            user = User.objects.get(pk=user_id)
        except Exception as e:
            print(e)
            return None

        return user, token
