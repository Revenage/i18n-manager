from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        permission_classes = (permissions.IsAdminUser)
        if permission_classes:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=self.request.user.id)
