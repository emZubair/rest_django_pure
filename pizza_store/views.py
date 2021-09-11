from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser

from .models import Pizzeria
from .erializers import (PizzeriaListSerializer, PizzeriaDetailsSerializer,
                         CreateUserSerializer)


class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaDetailsAPIView(generics.RetrieveAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer


class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer


class PizzeriaUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer


class PizzeriaDestroyAPIView(generics.DestroyAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer
