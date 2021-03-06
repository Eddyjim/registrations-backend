# Generated by Django 3.2.5 on 2021-07-09 06:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20210709_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='current_capacity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 6, 56, 41, 439003)),
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('event', 'person')},
        ),
        migrations.CreateModel(
            name='RegistrationQueue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registration.person')),
            ],
        ),
    ]
