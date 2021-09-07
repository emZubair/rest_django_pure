from django.urls import reverse
from rest_framework import serializers

from .models import Pizzeria, PizzaImage


class PizzeriaListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = ('id', 'pizzeria_name', 'city', 'state', 'description', 'logo_image',
                  'is_active', 'email', 'absolute_url')

    def get_absolute_url(self, obj):
        return reverse('pizza_details', args=(obj.pk,))


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PizzaImage
        fields = ('id', 'image', 'image_title', 'uploaded_at')


class PizzeriaDetailsSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Pizzeria
        fields = ('pizzeria_name', 'city', 'phone_number', 'state',
                  'description', 'is_active', 'email', 'update', 'delete', 'images')

    def get_update(self, obj):
        return reverse('pizza_update', args=(obj.pk,))

    def get_delete(self, obj):
        return reverse('pizza_delete', args=(obj.pk,))
