from rest_framework import serializers

from image.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Image
        fields = ['url', 'base_64']

    def create(self, validated_data):
        # create an image object
        image = Image(**validated_data)
        image.save()
        # return the correct uuid for the API response
        validated_data["id"] = image.id
        return Image(**validated_data)
