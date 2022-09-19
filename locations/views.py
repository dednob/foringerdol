from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


@api_view(['GET'])
def location_api_viewLocation(request, pk=None):
    id = pk
    if id is not None:
        location = Location.objects.get(id=id)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def location_api_createLocation(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def location_api_completeUpdate(request, pk=None):
    id = pk
    location = Location.objects.get(id=id)
    serializer = LocationSerializer(location, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Complete Data Updated'})
    return Response(serializer.errors)


@api_view(['PATCH'])
def location_api_partialUpdate(request, pk=None):
    id = pk
    location = Location.objects.get(pk=id)
    serializer = LocationSerializer(location, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
def location_api_delete(request, pk=None):
    id = pk
    location = Location.objects.get(pk=id)
    location.delete()
    return Response({'msg': 'Data Deleted'})
