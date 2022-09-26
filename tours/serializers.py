from rest_framework import serializers
from .models import Tour


class TourReadSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField('location_name')

    def location_name(self, obj):
        return {obj.location.locations_name,
                obj.location.id}
    class Meta:
        model = Tour
        fields = ['id', 'tour_name',  'price', 'location', 'details', 'no_of_days', 'tour_image', 'banner_image', 'slug']

class TourSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Tour
        fields = ['id', 'tour_name',  'price', 'location', 'details', 'no_of_days', 'tour_image', 'banner_image', 'slug']
