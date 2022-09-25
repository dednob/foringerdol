from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()
    class Meta:
        model = Event
        fields = ['event_name','event_image', 'location', 'details', 'slug']
