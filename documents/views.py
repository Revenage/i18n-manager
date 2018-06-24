# from rest_framework import generics

from .models import Document
from .serializers import DocumentsSerializer

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework import authentication, permissions


class DocumentViewSet(ModelViewSet):
    # authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)
    # queryset = Document.objects.all()
    serializer_class = DocumentsSerializer

    # def list(self, request):
    #     queryset = Document.objects.all()
    #     serializer = DocumentsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Document.objects.all()
    #     document = get_object_or_404(queryset, pk=pk)
    #     serializer = DocumentsSerializer(document)
    #     return Response(serializer.data)

    # def create(self, request):
    #     document = Document.objects.create_document(
    #         name=validated_data['name'],  # HERE
    #     )
    #     return document

    #     pass

    # def destroy(self, request, pk=None):
    #     queryset = self.get_object(pk)
    #     document = get_object_or_404(queryset, pk=pk)
    #     document.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #     pass
