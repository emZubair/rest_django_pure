from rest_framework import generics

from .models import Pizzeria
from .erializers import PizzeriaListSerializer, PizzeriaDetailsSerializer


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
