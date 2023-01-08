# Generated by Django 4.1 on 2023-01-08 09:40

from django.db import migrations, models
import pictures.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.ImageField(null=True, upload_to=pictures.models.generate_filename)),
                ('promotionOne', models.ImageField(null=True, upload_to=pictures.models.generate_filename)),
                ('promotionTwo', models.ImageField(null=True, upload_to=pictures.models.generate_filename)),
                ('footer', models.ImageField(null=True, upload_to=pictures.models.generate_filename)),
            ],
        ),
    ]