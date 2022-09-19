from django.db import models


# Create your models here.
class Location(models.Model):
    choices = [('domestic', 'Domestic'),
               ('international', 'International'),
               ]
    locations_name = models.CharField(max_length=200)
    # cover_image =
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=1500)
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=50, choices=choices, default='domestic')
    # def __str__(self):
    #     return self.locations_name
