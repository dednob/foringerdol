from rest_framework import serializers
from .models import Event
from locations.models import *
from locations.serializers import *

class EventReadSerializer(serializers.ModelSerializer):

    location = serializers.SerializerMethodField('location_name',  read_only = True)
    packages = serializers.SerializerMethodField('event_packages', read_only=True)

    def location_name(self, obj):
        location_instance = Location.objects.get(id=obj.location.id)

        return LocationSerializerRef(location_instance).data

    def event_packages(self, obj):
        from packages.serializers import PackageSerializerRef
        return PackageSerializerRef(obj.packages.all(), many=True).data

    class Meta:
        model = Event
        fields = [ 'id','event_name', 'trending', 'event_image','banner_image', 'location', 'details', 'slug', 'packages']

class EventSerializer(serializers.ModelSerializer):
    
    
   
    class Meta:
        model = Event
        fields = [ 'id','event_name','trending', 'event_image','banner_image', 'location', 'details', 'slug']



class EventSerializerRef(serializers.ModelSerializer):   
   
    class Meta:
        model = Event
        fields = [ 'id','event_name','trending']