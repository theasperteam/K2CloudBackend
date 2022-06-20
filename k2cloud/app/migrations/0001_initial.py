# Generated by Django 4.0.5 on 2022-06-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
    ]
