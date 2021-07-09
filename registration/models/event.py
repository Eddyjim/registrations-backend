from django.db import models

from registration.models.location import Location
from registration.models.person import Person


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=False)
    capacity = models.PositiveIntegerField(null=False, default=0)
    current_capacity = models.PositiveIntegerField(null=False, default=0)
    enabled = models.BooleanField(null=False, default=False)


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=False)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    attended = models.BooleanField(default=False, null=False)
    seat_number = models.PositiveIntegerField(null=True)

    class Meta:
        unique_together = ('event', 'person')


class HandWashRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    timestamp = models.DateTimeField(auto_now=True)


class RegistrationQueue(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    timestamp = models.DateTimeField(auto_now=True)
