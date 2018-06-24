from rest_framework.serializers import ModelSerializer
from .models import Document


class DocumentsSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name', 'owner', 'created_date',
                  'published_date', 'data')
