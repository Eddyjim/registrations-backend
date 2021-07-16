from django import forms
from django.contrib import admin

# Register your models here.
from registration.models import Person, DocumentType, Event, Location
from registration.models.event import TempRegistration, Registration
from registration.models.text import Text, Questions


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('document_id', 'first_name', 'first_surname')
    list_display = ('document_type_name', 'document_id', 'full_name')

    def document_type_name(self, obj):
        return obj.document_type.name

    def full_name(self, obj):
        return " ".join((obj.first_name, obj.middle_name if obj.middle_name else "", obj.first_surname,
                         obj.second_surname if obj.second_surname else ""))


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


# admin.site.register(Person, PersonAdmin)
# admin.site.register(DocumentType, DocumentTypeAdmin)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'location_name', 'date')
    fields = ('label', 'date', 'location', 'capacity', 'current_capacity', 'enabled')

    def location_name(self, obj):
        """

        """
        return obj.location.name


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')


@admin.register(TempRegistration)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_label', 'amount')

    def event_label(self, obj):
        return obj.event.label


@admin.register(Text)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(Registration)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_label', 'person_id', 'attended', 'seat_number')
    list_filter = ['event__label', 'event__date','person__document_id']

    # def event_label(self, obj):
    #     return obj.event.label
    #
    def person_id(self, obj):
        return obj.person.document_id