import json
from django.db.utils import IntegrityError
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from registration.models import Registration, Event, Person
from registration.models.event import TempRegistration
from registration.models.text import Text
from registration.serializers.event import PreRegistrationSerializer, HandWashRegistrationSerializer, EventSerializer


@api_view(['GET'])
def events(request):
    """

    :param request:
    :return:
    """
    enabled_events = Event.objects.filter(enabled=True)
    event_serializer = EventSerializer(enabled_events, many=True)

    return JsonResponse(event_serializer.data, status=status.HTTP_200_OK, safe=False)


@api_view(['POST', 'DELETE'])
def tempRegistration(request):
    """

    """
    if request.method == 'POST':

        body = json.loads(request.body)
        event = Event.objects.get(id=body['event_id'])
        temp = TempRegistration(event=event, amount=body['amount'])
        if event.current_capacity + body['amount'] <= event.capacity:
            event.current_capacity += body['amount']
            event.save()
            temp.save()
            return JsonResponse({'temp_id': temp.id, 'message': Text.objects.get(name='timelimit').value},
                                status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'error': Text.objects.get(name='maxcapacity').value},
                                status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        temp_registration_id = request.query_params.get('temp_registration_id', None)

        if temp_registration_id:
            temp_registration = TempRegistration.objects.get(id=temp_registration_id)
            event = temp_registration.event
            event.current_capacity = event.current_capacity - temp_registration.amount
            event.save()
            temp_registration.delete()
            return JsonResponse({"message": "deleted"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def delete_preregistration(request):
    if request.method == 'POST':
        pre_registration_data = JSONParser().parse(request)
        temp_registration_id = pre_registration_data['temp_registration_id']

        if temp_registration_id:
            temp_registration = TempRegistration.objects.get(id=temp_registration_id)
            event = registration.event
            event.current_capacity = event.current_capacity - temp_registration.amount
            event.save()
            temp_registration.delete()
            return JsonResponse({"message": "deleted"}, status=status.HTTP_200_OK)


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
    # elif request.method == 'DELETE':
    #     temp_registration_id = request.query_params.get('temp_registration_id', None)
    #     if temp_registration_id:
    #         temp_registration = TempRegistration.objects.get(id=temp_registration_id)
    #         event = registration.event
    #         event.current_capacity = event.current_capacity - temp_registration.amount
    #         event.save()
    #         temp_registration.delete()


@api_view(['POST', 'DELETE'])
def registration(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        registration_data = JSONParser().parse(request)
        people = registration_data['people']
        event = Event.objects.get(id=registration_data['event'])
        registrations = []
        for p in people:
            person = Person.objects.get(document_type__id=p["document_type"], document_id=p["document_id"])
            try:
                reg = Registration(person=person, event=event)
                reg.save()
                registrations.append(reg.id)
            except IntegrityError:
                document = {
                    'document_type': person.document_type.name,
                    'document_id': person.document_id
                }
                message = Text.objects.get(name='already-registered')
                try:
                    tempRegistration = TempRegistration.objects.get(id=registration_data['temp_registration'])
                    event = tempRegistration.event
                    event.current_capacity = event.current_capacity - tempRegistration.amount
                    event.save()
                    tempRegistration.delete()
                except:
                    pass
                return JsonResponse({'message': message.value, 'person': document}, status=status.HTTP_400_BAD_REQUEST)
        try:
            tempRegistration = TempRegistration.objects.get(id=registration_data['temp_registration'])
            tempRegistration.delete()
        except:
            pass

        return JsonResponse({'registrations': registrations}, status=status.HTTP_201_CREATED)


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
