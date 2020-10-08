from rest_framework import serializers, response, status
from rest_framework.fields import CharField
from rest_framework.response import Response

from image.helpers import get_file_type
from image.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'url', 'base_64', 'remote_location', 'raw_file']
        read_only_fields = ('id', 'url', 'remote_location', 'raw_file')

    def create(self, validated_data):
        # create an image object
        if get_file_type(validated_data["base_64"]):
            image = Image(**validated_data)
            image.save()
            # return the correct uuid for the API response
            validated_data["id"] = image.id
            return Image(**validated_data)

        else:
            raise serializers.ValidationError({"error": "Image cannot be decoded"})

    def update(self, instance, validated_data):
        validated_data.pop('remote_location', None)  # prevent myfield from being updated
        validated_data.pop('base_64', None)  # prevent myfield from being updated

        return super().update(instance, validated_data)


class JpegImageSerializer(serializers.Serializer):

    def convert(self, image):
        print(image)
        return Response({"message": "success"})
