from rest_framework import serializers
from .models import Hotel


class HotelReadSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField('location_name')

    def location_name(self, obj):
        return {obj.location.locations_name,
                obj.location.id}

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name',  'price', 'location', 'details', 'slug','hotel_image', 'banner_image']

class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name',  'price', 'location', 'details', 'slug','hotel_image', 'banner_image']
