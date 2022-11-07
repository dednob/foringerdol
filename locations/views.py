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
    try:
        if id is not None:
            location = Location.objects.get(id=id)
            serializer = LocationSerializer(location)
            return Response({
                'code': request.status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })

        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response({
                'code': request.status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })

    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def location_by_category(request, pk):  
    try:  
        location = Location.objects.filter(category = pk)
        serializer = LocationSerializer(location, many=True)
        return Response({
                'code': request.status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })

    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_location(request):
    try:
        location_data = request.data
        
        if 'location_image' in location_data and location_data['event_image']!=None:
            fmt, img_str = str(location_data['location_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            location_data['location_image'] = img_file

        if 'banner_image' in location_data and location_data['banner_image']!=None:
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
            
            return Response({
                'code': request.status.HTTP_200_OK,
                'response': "Data created successfully",
                'data': serializer.data

            })
        else:
            return Response({
                'code': request.status.HTTP_400_BAD_REQUEST,
                'response': "Data not found",
                'error': serializer.errors
            })

    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def complete_update(request, pk=None):
    try:
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
            
            return Response({
                'code': request.status.HTTP_200_OK,
                'response': "Data created successfully",
                'data': serializer.data

            })
        else:
            return Response({
                'code': request.status.HTTP_400_BAD_REQUEST,
                'response': "Data not found",
                'error': serializer.errors
            })

    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


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
    try:
        location = Location.objects.get(pk=id)
        location.delete()
        return Response({'code': request.status.HTTP_200_OK,'msg': 'Data Deleted'})

    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
