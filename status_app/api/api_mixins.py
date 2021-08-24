from .serializer import StatusSerializer


class APIMixins(object):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    lookup_field = 'id'
