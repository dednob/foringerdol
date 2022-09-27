from rest_framework import serializers
from .models import Tour
from locations.models import *
from locations.serializers import *


class TourReadSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField('location_name')

    def location_name(self, obj): 
        location_instance = Location.objects.get(id=obj.location.id)
        
        return LocationSerializer(location_instance).data
    class Meta:
        model = Tour
        fields = ['id', 'tour_name',  'price', 'location', 'details', 'no_of_days', 'tour_image', 'banner_image', 'slug']

class TourSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Tour
        fields = ['id', 'tour_name',  'price', 'location', 'details', 'no_of_days', 'tour_image', 'banner_image', 'slug']
