from .serializer import StatusSerializer
from rest_framework.throttling import SimpleRateThrottle


class APIMixins(object):
    serializer_class = StatusSerializer

    lookup_field = 'id'


class OneRequestPerDay(SimpleRateThrottle):
    rate = '1/day'

    def get_cache_key(self, request, view):
        return "throttle_{viewid}_{indent}".format(
            viewid=id(view),
            indent=request
        )


