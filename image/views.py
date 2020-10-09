from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from image.models import Image
from image.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be uploaded in bulk.
    """
    queryset = Image.objects.all().order_by('-created')
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
