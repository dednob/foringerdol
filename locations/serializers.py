from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField('event_count')

      
    def event_count(self, obj):
        return obj.events.count()

    class Meta:
        model = Location
        fields = ['locations_name', 'category', 'details', 'slug', 'location_image','events']
  