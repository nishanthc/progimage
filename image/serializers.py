from rest_framework import serializers

from image.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Image
        fields = ['url', 'base_64']

    def create(self, validated_data):
        print(validated_data)
        Image(**validated_data).save()
        return Image(**validated_data)
