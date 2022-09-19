import uuid
from django.db import models

def generate_filename(instance, filename):
   extension = filename.split('.')[-1]
   new_filename = "foringLocation_%s.%s" % (uuid.uuid4(), extension)
   return new_filename



# Create your models here.
class Location(models.Model):
    choices = [('domestic', 'Domestic'),
               ('international', 'International'),
               ]
    locations_name = models.CharField(max_length=200)
    location_image = models.ImageField(upload_to=generate_filename, null=True)
    details = models.CharField(max_length=1500)
    slug = models.SlugField(max_length=255)
    category = models.CharField(max_length=50, choices=choices, default='domestic')

    # def __str__(self):
    #     return self.locations_name
