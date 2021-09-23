from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework import permissions

from .models import Pizzeria
from .erializers import (PizzeriaListSerializer, PizzeriaDetailsSerializer,
                         CreateUserSerializer)


class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PizzeriaDetailsAPIView(generics.RetrieveAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PizzeriaUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PizzeriaDestroyAPIView(generics.DestroyAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer

    def get_serializer_context(self):
        return {'request': self.request}
