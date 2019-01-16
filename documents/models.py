from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.contrib.postgres.fields import JSONField


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=255, default='Untitled')
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='documents')
    created_date = models.DateTimeField(
        null=True, blank=True, default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)

    data = JSONField(null=True, blank=True)
    description = models.CharField(blank=True, max_length=255, default='')

    def __str__(self):
        return self.name
