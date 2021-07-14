from rest_framework import serializers

from registration.models.text import Text


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = ('id', 'name', 'value')