import requests
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from registration.models import Person, DocumentType
from registration.serializers.person import PersonSerializer, DocumentTypeSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Person.objects.all().order_by('first_surname')
    serializer_class = PersonSerializer


@api_view(['GET', 'POST', 'DELETE'])
def person(request):
    """

    :param request:
    :return:
    """

    if request.method == 'GET':
        persons = Person.objects.all()
        document_id = request.query_params.get('document_id', None)
        document_type = request.query_params.get('document_type', None)
        if document_id:
            persons = persons.filter(document_type__exact=document_type,document_id__exact=document_id)
        person_serializer = PersonSerializer(persons, many=True)

        return JsonResponse(person_serializer.data, safe=False)
    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person_id = request.query_params.get('person_id', None)
        if person_id:
            Person.objects.filter(person_id=person_id).delete()
            return JsonResponse(status=status.HTTP_200_OK)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def document_type(_):
    document_types = DocumentType.objects.all()
    document_type_serializer = DocumentTypeSerializer(document_types, many=True)

    return JsonResponse(document_type_serializer.data, safe=False)
