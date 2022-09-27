from rest_framework import serializers
from .models import Event
from locations.models import *
from locations.serializers import *

class EventReadSerializer(serializers.ModelSerializer):
    
    location = serializers.SerializerMethodField('location_name',  read_only = True)

    def location_name(self, obj): 
        location_instance = Location.objects.get(id=obj.location.id)
        
        return LocationSerializer(location_instance).data

    class Meta:
        model = Event
        fields = [ 'id','event_name', 'event_image','banner_image', 'location', 'details', 'slug']

class EventSerializer(serializers.ModelSerializer):
    
    
   
    class Meta:
        model = Event
        fields = [ 'id','event_name', 'event_image','banner_image', 'location', 'details', 'slug']
