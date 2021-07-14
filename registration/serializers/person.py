from rest_framework import serializers

from registration.models import Person, DocumentType


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'document_type', 'document_id', 'first_name', 'middle_name', 'first_surname', 'second_surname', 'birthday',
            'city', 'address', 'phone')


class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
        fields = ('id', 'name', 'description')
