from rest_framework import serializers
from .models import Package
from events.models import *
from events.serializers import *


class PackageReadSerializer(serializers.ModelSerializer):

    event = serializers.SerializerMethodField('event_name', read_only=True)

    def event_name(self, obj):
        event_instance = Event.objects.get(id=obj.event.id)

        return EventSerializerRef(event_instance).data

    class Meta:
        model = Package
        fields = ['id', 'package_name', 'package_image', 'banner_image', 'price', 'details', 'slug', 'event']


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = ['id', 'package_name', 'package_image', 'banner_image', 'price', 'details', 'slug', 'event']


class PackageSerializerRef(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = ['id', 'package_name', 'price']
