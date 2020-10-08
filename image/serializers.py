from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.response import Response

from image.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'base_64', 'remote_location']
        read_only_fields = ('id', 'url', 'remote_location', 'base_64')

    def create(self, validated_data):
        # create an image object
        image = Image(**validated_data)
        image.save()
        # return the correct uuid for the API response
        validated_data["id"] = image.id
        return Image(**validated_data)


class JpegImageSerializer(serializers.Serializer):

    def convert(self, image):
        print(image)
        return Response({"message": "success"})
