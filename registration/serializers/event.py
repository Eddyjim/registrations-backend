from rest_framework import serializers

from registration.models import Registration
from registration.models.event import HandWashRegistration


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


class RegistrationQueueSerializer(serializers.ModelSerializer):
    person_id = serializers.CharField(source="person")

    class Meta:
        model = HandWashRegistration
        fields = ('person_id')
