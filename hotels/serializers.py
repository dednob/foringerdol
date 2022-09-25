from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()
    class Meta:
        model = Hotel
        fields = ['hotel_name','hotel_image', 'price', 'location', 'details', 'slug']
