from django.db import models
from locations.models import Location
import uuid


def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "foringEvent_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to=generate_filename, null=True)
    details = models.CharField(max_length=1500)
    slug = models.SlugField(max_length=255)
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.event_name
