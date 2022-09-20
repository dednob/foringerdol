from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name','hotel_image', 'price', 'location', 'details', 'slug']
