# Generated by Django 4.1 on 2023-01-08 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='journey_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
