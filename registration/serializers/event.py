from rest_framework import serializers

from registration.models import Registration
from registration.models.event import HandWashRegistration, Event, TempRegistration


class PreRegistrationSerializer(serializers.ModelSerializer):
    person_id = serializers.CharField(source="person")
    event_id = serializers.CharField(source="event")

    class Meta:
        model = Registration
        fields = ('event_id', 'person_id')


class RegistrationSerializer(serializers.ModelSerializer):
    person_id = serializers.CharField(source="person")
    event_id = serializers.CharField(source="event")

    class Meta:
        model = Registration
        fields = ('event_id', 'person_id', 'attended', 'seat_number')


class HandWashRegistrationSerializer(serializers.ModelSerializer):
    person_id = serializers.CharField(source="person")

    class Meta:
        model = HandWashRegistration
        fields = ('person_id')


class EventSerializer(serializers.ModelSerializer):
    location_name = serializers.ReadOnlyField(source='location.name')
    location_address = serializers.ReadOnlyField(source='location.address')

    class Meta:
        model = Event
        fields = ('id', 'label', 'date', 'location_name', 'location_address', 'capacity', 'current_capacity')


class RegistrationQueueSerializer(serializers.ModelSerializer):
    person_id = serializers.CharField(source="person")

    class Meta:
        model = HandWashRegistration
        fields = ('person_id')


class TempRegistrationSerializer(serializers.ModelSerializer):
    event_id = serializers.CharField(source="event")

    class Meta:
        model: TempRegistration
        fields = ('id', 'event_id', 'amount')
