from rest_framework import serializers

from registration.models.text import Text, Questions


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = ('id', 'name', 'value')


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('id', 'value')