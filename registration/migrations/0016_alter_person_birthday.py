# Generated by Django 3.2.5 on 2021-07-22 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_alter_person_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2021, 7, 22, 2, 2, 31, 787773)),
        ),
    ]