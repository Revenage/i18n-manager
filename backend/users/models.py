from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db import models


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
