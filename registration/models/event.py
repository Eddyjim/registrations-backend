import datetime

from django.contrib import admin
from django.db import models

from registration.models.location import Location
from registration.models.person import Person


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(null=False, max_length=500)
    date = models.DateTimeField(null=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=False)
    capacity = models.PositiveIntegerField(null=False, default=0)
    current_capacity = models.PositiveIntegerField(null=False, default=0)
    enabled = models.BooleanField(null=False, default=False)

    #
    # @admin.display
    # def location_name(self):
    #     return self.location.name

    @property
    def location_name(self):
        return self.location.name

    @property
    def location_address(self):
        return self.location.address


class TempRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=False)
    amount = models.PositiveIntegerField(null=False)
    timestamp = models.DateTimeField(auto_now=True)


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=False)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    attended = models.BooleanField(default=False, null=False)
    seat_number = models.PositiveIntegerField(null=True)

    def person_id(self):
        return self.person.id

    def event_label(self):
        return self.event.label

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
