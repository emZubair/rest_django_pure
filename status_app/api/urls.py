from django.urls import path
from .views import (StatusCreateAPIView, StatusUpdateAPIView, StatusDetailsAPIView,
                    StatusListAPIView, StatusDeleteAPIView)

urlpatterns = [
    path(r'^$', StatusListAPIView.as_view()),
    path(r'^create/$', StatusCreateAPIView.as_view()),
    path(r'(?P<id>.*)/$', StatusCreateAPIView.as_view()),
    path(r'^(?P<id>.*)/update/$', StatusCreateAPIView.as_view()),
    path(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]
