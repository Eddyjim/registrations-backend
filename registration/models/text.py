from django.db import models


class Text(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    value = models.CharField(max_length=1000)


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=1000)
