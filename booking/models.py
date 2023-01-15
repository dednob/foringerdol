from django.db import models
from locations.models import Location
from events.models import Event
from django.utils.translation import gettext as _
from datetime import date

# Create your models here.



class Booking(models.Model):
    
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    contact_number = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField(null = True, blank = True)
    num_person_Adult = models.IntegerField(default=0, null=True)
    num_person_Child = models.IntegerField(default=0, null=True)
    journey_date = models.DateField(_("Date"), default=date.today)
    payment_status = models.BooleanField(default=False)
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE, related_name='booking')
    events = models.ForeignKey(Event, default=None, on_delete=models.CASCADE, related_name='booking')
 