from django.db import models

from django.conf import settings


def upload_update_iamge(instance, image_name):
    return f'updates/{instance.user}/{image_name}'


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    """Manager for Status Model"""

    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    """Model to store user status"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(upload_to=upload_update_iamge, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    objects = StatusManager()

    def __str__(self):
        return self.content or ""

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'