from django.db import models
from locations.models import Location


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    # cover_image =
    details = models.CharField(max_length=1500)
    slug = models.SlugField(max_length=255)
    location = models.ForeignKey(Location, default=None, on_delete=models.DO_NOTHING)
