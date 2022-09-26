import uuid
from django.db import models
from locations.models import Location


def generate_filename(instance, filename):
   extension = filename.split('.')[-1]
   new_filename = "foringTour_%s.%s" % (uuid.uuid4(), extension)
   return new_filename

# Create your models here.
class Tour(models.Model):
    tour_name = models.CharField(max_length=200)
    tour_image = models.ImageField(upload_to=generate_filename, null=True)
    banner_image = models.ImageField(upload_to=generate_filename, null=True)
    price = models.FloatField()
    details = models.TextField(null=True)
    no_of_days = models.IntegerField()
    slug = models.SlugField(max_length=255, null=True, unique=True)
    location = models.ForeignKey(Location, default=None, on_delete=models.DO_NOTHING)
