from rest_framework.serializers import ModelSerializer, ReadOnlyField, Field
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        # 'is_active', 'is_staff', 'token'
        fields = ('email', 'username', 'id')
