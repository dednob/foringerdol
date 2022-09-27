from rest_framework import serializers
from .models import Hotel
from locations.models import *
from locations.serializers import *

class HotelReadSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField('location_name')

    def location_name(self, obj): 
        location_instance = Location.objects.get(id=obj.location.id)
        
        return LocationSerializer(location_instance).data

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name',  'price', 'location', 'details', 'slug','hotel_image', 'banner_image']

class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name',  'price', 'location', 'details', 'slug','hotel_image', 'banner_image']
