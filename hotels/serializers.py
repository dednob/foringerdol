from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField('location_name')

    def location_name(self, obj):
        return {obj.location.locations_name,
                obj.location.id}
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_image', 'price', 'location', 'details', 'slug']
