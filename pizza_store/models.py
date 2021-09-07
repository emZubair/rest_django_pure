from django.db import models
from django.core.validators import RegexValidator


PIZZERIA_IMAGE_PATH = 'pizzeriaImages'


class Pizzeria(models.Model):
    pizzeria_name = models.CharField(max_length=32, blank=False)
    city = models.CharField(max_length=16, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    phone_number = models.IntegerField(validators=[RegexValidator(regex=r'^\1?\d{9,10}$')],
                                       null=True, blank=True)
    description = models.TextField(blank=True)
    logo_image = models.ImageField(upload_to=PIZZERIA_IMAGE_PATH, blank=True,
                                   default=f'{PIZZERIA_IMAGE_PATH}/default.png')
    email = models.EmailField(max_length=32, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.pizzeria_name} :{self.is_active}'


class PizzaImage(models.Model):
    pizzeria = models.ForeignKey(Pizzeria, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    image = models.ImageField(upload_to='photos', default=f'{PIZZERIA_IMAGE_PATH}/default.png')
    image_title = models.CharField(max_length=32, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-uploaded_at',)

    def __str__(self):
        return self.image_title
