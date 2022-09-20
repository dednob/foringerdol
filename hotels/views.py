from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile



@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
# @permission_classes([IsAuthenticated])
def createHotel(request):
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        if 'hotel_image' in serializer:
            fmt, img_str = str(serializer['hotel_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            serializer['hotel_image'] = img_file
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def completeUpdateHotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(id=id)
    serializer = HotelSerializer(hotel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        if 'hotel_image' in serializer:
            fmt, img_str = str(serializer['hotel_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            serializer['hotel_image'] = img_file
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def partialUpdateHotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(pk=id)
    serializer = HotelSerializer(hotel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteHotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(pk=id)
    hotel.delete()
    return Response({'msg': 'Data Deleted'})
