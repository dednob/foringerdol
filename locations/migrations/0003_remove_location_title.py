# Generated by Django 4.1 on 2022-09-19 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='title',
        ),
    ]
