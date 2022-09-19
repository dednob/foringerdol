from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


@api_view(['GET'])
def getHotel(request, pk=None):
    id = pk
    if id is not None:
        hotel = Hotel.objects.get(id=id)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createHotel(request):
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def completeUpdateHotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(id=id)
    serializer = HotelSerializer(hotel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Complete Data Updated'})
    return Response(serializer.errors)


@api_view(['PATCH'])
def partialUpdateHotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(pk=id)
    serializer = HotelSerializer(hotel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
def deleteHotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(pk=id)
    hotel.delete()
    return Response({'msg': 'Data Deleted'})
