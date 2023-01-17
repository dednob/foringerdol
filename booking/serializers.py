from rest_framework import serializers
from locations.serializers import *
from events.serializers import *
from .models import Booking

from locations.models import *
from events.models import *

class BookingSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Booking
        fields = ['id', 'name', 'email', 'contact_number', 'details','num_person_Adult', 'num_person_Child', 'journey_date', 'payment_status', 'location', 'events']

class BookingReadSerializer(serializers.ModelSerializer):
    
    location = serializers.SerializerMethodField('location_title', read_only=True)
    events = serializers.SerializerMethodField('event_title', read_only=True)

    def location_title(self, obj):
        location_instance = Location.objects.get(id = obj.location.id)
        return LocationSerializerRef(location_instance).data

    def event_title(self, obj):
        event_instance = Event.objects.get(id = obj.events.id)
        return EventSerializerRef(event_instance).data
    
    class Meta:
        model = Booking
        fields = ['id', 'name', 'email', 'contact_number', 'details','num_person_Adult', 'num_person_Child', 'journey_date', 'payment_status', 'location', 'events']
