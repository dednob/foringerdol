from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    # location = serializers.StringRelatedField()
    location = serializers.SerializerMethodField('location_name')

    def location_name(self, obj):
        return {obj.location.locations_name,
                obj.location.id}

    class Meta:
        model = Event
        fields = [ 'id','event_name', 'event_image', 'location', 'details', 'slug']
