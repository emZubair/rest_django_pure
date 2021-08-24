from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from status_app.models import Status
from status_app.api.serializer import StatusSerializer

from .api_mixins import APIMixins


class StatusListSearchAPIView(APIMixins, APIView):
    """List API view with Search"""

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(data=qs, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class StatusAPIView(APIMixins, generics.ListAPIView):

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q', None)
        if query:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateAPIView(APIMixins, generics.CreateAPIView):
    queryset = Status.objects.all()

    def perform_create(self, serializer):
        serializer.save(self.request.user)


class StatusDetailsAPIView(APIMixins, generics.RetrieveAPIView):

    # def get_queryset(self):
    #     return Status.objects.all()

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        return Status.objects.get(id=kwargs.get('id'))


class StatusUpdateAPIView(APIMixins, generics.UpdateAPIView):

    queryset = Status.objects.all()


class StatusDeleteAPIView(APIMixins, generics.DestroyAPIView):
    queryset = Status.objects.all()
