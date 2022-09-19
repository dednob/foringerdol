from django.db import models
from locations.models import Location


# Create your models here.
class Tour(models.Model):
    tour_name = models.CharField(max_length=200)
    # cover_image =
    price = models.FloatField()
    details = models.CharField(max_length=1500)
    no_of_days = models.IntegerField()
    location = models.ForeignKey(Location, default=None, on_delete=models.DO_NOTHING)
