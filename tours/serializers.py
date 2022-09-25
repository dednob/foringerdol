from rest_framework import serializers
from .models import Tour


class TourSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()
    class Meta:
        model = Tour
        fields = ['tour_name','tour_image', 'price', 'location', 'details', 'no_of_days','slug']
