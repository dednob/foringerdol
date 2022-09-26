from rest_framework import serializers
from .models import Event


class EventReadSerializer(serializers.ModelSerializer):
    
    
    location = serializers.SerializerMethodField('location_name',  read_only = True)

    def location_name(self, obj):
        return {obj.location.locations_name,
                obj.location.id}

    class Meta:
        model = Event
        fields = [ 'id','event_name', 'event_image','banner_image', 'location', 'details', 'slug']

class EventSerializer(serializers.ModelSerializer):
    
    
   
    class Meta:
        model = Event
        fields = [ 'id','event_name', 'event_image','banner_image', 'location', 'details', 'slug']
