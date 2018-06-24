from rest_framework import serializers
from . import models


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = ('id', 'name', 'owner', 'created_date', 'published_date')
