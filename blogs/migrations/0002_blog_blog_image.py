# Generated by Django 4.1 on 2022-09-19 09:48

import blogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(null=True, upload_to=blogs.models.generate_filename),
        ),
    ]
