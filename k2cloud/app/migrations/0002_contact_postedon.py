# Generated by Django 4.0.5 on 2022-06-21 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='postedOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 16, 56, 54, 428158)),
        ),
    ]
