from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from status_app.models import Status
from rest_framework.mixins import CreateModelMixin
from status_app.api.serializer import StatusSerializer
from accounts.pagination import PureRestPagination

from .api_mixins import APIMixins, OneRequestPerDay


class StatusListSearchAPIView(APIMixins, generics.RetrieveAPIView):
    """List API view with Search"""

    throttle_classes = [OneRequestPerDay]
    pagination_class = PureRestPagination
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'pk'
    #
    # def get(self, request, format=None):
    #     qs = Status.objects.all()
    #     serializer = StatusSerializer(data=qs, many=True)
    #     serializer.is_valid()
    #     return Response(serializer.data)

# CREATE MODEL MIXIN === POST
# UPDATE MODEL MIXIN === PUT
# DELETE MODEL MIXIN === DELETE


class StatusAPIView(APIMixins, mixins.CreateModelMixin, generics.ListAPIView):
    search_fields = ('content',)
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.kwargs.get('username')
    #     if query:
    #         qs = qs.filter(content__icontains=query)
    #
    #     return qs or Status.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(self.request.user)


class StatusDetailsAPIView(APIMixins, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                           generics.RetrieveAPIView):

    # def get_queryset(self):
    #     return Status.objects.all()

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        return Status.objects.get(id=kwargs.get('id'))

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateMixinStatus(CreateModelMixin):
    pass
