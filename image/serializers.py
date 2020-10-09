import base64

from django.core.files.base import ContentFile
from rest_framework import serializers, response, status
from rest_framework.fields import CharField
from rest_framework.response import Response

from image.helpers import get_file_type, valid_remote_image, base_64_upload
from image.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'url', 'base_64', 'remote_location', 'raw_file','extension']
        read_only_fields = ('id', 'url', 'raw_file','extension')

    def create(self, validated_data):
        # create an image object
        image = Image(**validated_data)

        if validated_data.get("base_64", None):
            file_type = get_file_type(validated_data["base_64"])
            if not file_type:
                raise serializers.ValidationError({"error": "Image cannot be decoded"})
            else:
                image.extension = file_type
        if validated_data.get("remote_location", None):
            image_check = valid_remote_image(validated_data["remote_location"])
            if not image_check:
                raise serializers.ValidationError({"error": "Image cannot be downloaded"})
            else:
                success, file_type, base_64 = image_check
                image.base_64 = base_64
                image.extension = file_type
                validated_data["base_64"] = image.base_64

        validated_data["extension"] = image.extension

        image.save()
        # return the correct uuid for the API response
        validated_data["id"] = image.id
        f_data = ContentFile(base64.b64decode(image.base_64))
        image.raw_file.save("file_name.jpg",f_data)
        validated_data["raw_file"] = image.raw_file

        return Image(**validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('remote_location', None)  # prevent myfield from being updated
        validated_data.pop('base_64', None)  # prevent myfield from being updated

        return super().update(instance, validated_data)


class JpegImageSerializer(serializers.Serializer):

    def convert(self, image):
        print(image)
        return Response({"message": "success"})
