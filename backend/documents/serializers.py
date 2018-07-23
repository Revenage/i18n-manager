from rest_framework.serializers import ModelSerializer, CurrentUserDefault
from .models import Document


class DocumentsSerializer(ModelSerializer):
    class Meta:
        model = Document
        owner = CurrentUserDefault()
        fields = ('id', 'name', 'owner', 'created_date',
                  'published_date', 'data')
        read_only_fields = ('owner',)