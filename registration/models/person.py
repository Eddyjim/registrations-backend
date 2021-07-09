from datetime import datetime

from django.db import models


class DocumentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT, null=False)
    document_id = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    middle_name = models.CharField(max_length=255, null=True)
    first_surname = models.CharField(max_length=255, null=False)
    second_surname = models.CharField(max_length=255, null=True)
    birthday = models.DateField(null=False, default=datetime.now())
    city = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=500, null=False)
    phone = models.IntegerField(null=False)

    class Meta:
        unique_together = ('document_type', 'document_id')


class Favorites(models.Model):
    PARENT = 'PR'
    CHILDREN = 'CH'
    SIBLING = 'SI'
    GRANDPARENT = 'GP'
    OTHER = 'OT'
    SPOUSE = 'SP'
    LABEL_CHOICES = [
        (PARENT, "Padre/Madre"),
        (CHILDREN, "Hijo/Hija"),
        (SIBLING, "Hermano/Hermana"),
        (GRANDPARENT, "Abuelo/Abuela"),
        (SPOUSE, "Esposo/Esposa"),
        (OTHER, "Otro")]
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, related_name='favorites')
    favorite = models.ForeignKey(Person, on_delete=models.CASCADE, null=False, related_name='favorite_of')
    label = models.CharField(max_length=2, choices=LABEL_CHOICES, null=False)
