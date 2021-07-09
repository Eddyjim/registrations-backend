from django.contrib import admin

# Register your models here.
from registration.models import Person, DocumentType


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('document_id', 'first_name', 'first_surname')
    list_display = ('document_type_name', 'document_id', 'full_name')

    def document_type_name(self, obj):
        return obj.document_type.name

    def full_name(self, obj):
        return " ".join((obj.first_name, obj.middle_name, obj.first_surname, obj.second_surname))


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

# admin.site.register(Person, PersonAdmin)
# admin.site.register(DocumentType, DocumentTypeAdmin)
