from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile
from django.utils.text import slugify


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def view_location(request, pk=None):
    id = pk
    if id is not None:
        location = Location.objects.get(id=id)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def location_by_category(request, pk):    
    location = Location.objects.filter(category = pk)
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)
    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_location(request):
    location_data = request.data
    
    if 'location_image' in location_data:
        fmt, img_str = str(location_data['location_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        location_data['location_image'] = img_file

    if 'banner_image' in location_data:
        fmt, img_str = str(location_data['banner_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        location_data['banner_image'] = img_file
    
    slug = slugify(location_data['locations_name'])
    suffix=1
    # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
    if Location.objects.filter(locations_name__exact=slug).exists():
        count=Location.objects.filter(locations_name__exact=slug).count()
        print(count)
        suffix+=count
        print("yes")
        slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
      
    else:
        slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
            
    location_data['slug']=slug
    serializer = LocationSerializer(data=location_data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def complete_update(request, pk=None):
    location_data = request.data
    if 'location_image' in location_data:
        fmt, img_str = str(location_data['location_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        location_data['location_image'] = img_file
    
    if 'banner_image' in location_data:
        fmt, img_str = str(location_data['banner_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        location_data['banner_image'] = img_file

    id = pk
    location = Location.objects.get(id=id)
    serializer = LocationSerializer(location, data=location_data)
    if serializer.is_valid():
        serializer.save()
        
        return Response({'msg': 'Complete Data Updated'})
    return Response(serializer.errors)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update(request, pk=None):
    id = pk
    location = Location.objects.get(pk=id)
    serializer = LocationSerializer(location, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_location(request, pk=None):
    id = pk
    location = Location.objects.get(pk=id)
    location.delete()
    return Response({'msg': 'Data Deleted'})
