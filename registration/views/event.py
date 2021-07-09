from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from registration.models import Registration
from registration.serializers.event import PreRegistrationSerializer, HandWashRegistrationSerializer


@api_view(['POST', 'DELETE'])
def pre_registration(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        pre_registration_data = JSONParser().parse(request)
        person_serializer = PreRegistrationSerializer(data=pre_registration_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        registration_id = request.query_params.get('registration_id', None)
        if registration_id:
            Registration.objects.get(registration_id=registration_id).delete()


@api_view(['GET', 'POST', 'DELETE'])
def registration(request):
    """

    :param request:
    :return:
    """
    pass


@api_view(['POST'])
def hand_wash_registration(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        hand_wash_registration_data = JSONParser().parse(request)
        hand_wash_registration_serializer = HandWashRegistrationSerializer(data=hand_wash_registration_data)
        if hand_wash_registration_serializer.is_valid():
            hand_wash_registration_serializer.save()
            return JsonResponse(hand_wash_registration_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(hand_wash_registration_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
