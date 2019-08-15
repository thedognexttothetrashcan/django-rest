from rest_framework.throttling import SimpleRateThrottle


class CommonThrottling(SimpleRateThrottle):

    rate = "10/m"

    def get_cache_key(self, request, view):
        return request.META.get("REMOTE_ADDR")


class CommonRateThrottling(SimpleRateThrottle):

    scope = "common"

    def get_cache_key(self, request, view):
        return request.META.get("REMOTE_ADDR")


class BlogThrottling(SimpleRateThrottle):

    rate = "100/m"

    def get_cache_key(self, request, view):
        return "blog_throttle:" + request.auth
