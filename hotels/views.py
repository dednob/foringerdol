from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Hotel
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile
from django.utils.text import slugify



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_hotel(request, pk=None):
    id = pk
    if id is not None:
        hotel = Hotel.objects.get(id=id)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def hotels_by_location(request, locationid):
    locationid = locationid
    hotels = Hotel.objects.filter(location= locationid)
    serializer = HotelReadSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_hotel(request):
    hotel_data = request.data
    if 'hotel_image' in hotel_data:
        fmt, img_str = str(hotel_data['hotel_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        hotel_data['hotel_image'] = img_file

    if 'banner_image' in hotel_data:
        fmt, img_str = str(hotel_data['banner_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        hotel_data['banner_image'] = img_file
    
    slug = slugify(hotel_data['hotel_name'])
    suffix=1
    # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
    if Hotel.objects.filter(hotel_name__exact=slug).exists():
        count=Hotel.objects.filter(hotel_name__exact=slug).count()
        print(count)
        suffix+=count
        print("yes")
        slug = "%s-%s" % (slugify(hotel_data['hotel_name']), suffix)
      
    else:
        slug = "%s-%s" % (slugify(hotel_data['hotel_name']), suffix)
            
    hotel_data['slug']=slug

    serializer = HotelSerializer(data=hotel_data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def complete_update_hotel(request, pk=None):
    hotel_data = request.data
    if 'hotel_image' in hotel_data:
        fmt, img_str = str(hotel_data['hotel_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        hotel_data['hotel_image'] = img_file

    if 'banner_image' in hotel_data:
        fmt, img_str = str(hotel_data['banner_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        hotel_data['banner_image'] = img_file
        
    id = pk
    hotel = Hotel.objects.get(id=id)
    serializer = HotelSerializer(hotel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_hotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(pk=id)
    serializer = HotelSerializer(hotel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_hotel(request, pk=None):
    id = pk
    hotel = Hotel.objects.get(pk=id)
    hotel.delete()
    return Response({'msg': 'Data Deleted'})
