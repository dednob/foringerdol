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
from rest_framework import status


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def view_location(request, slug=None):
    slug = slug
    try:
        if id is not None:
            location = Location.objects.get(slug=slug)
            serializer = LocationSerializer(location)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })

        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response({
                'code': status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
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
                'code': status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
    



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_location(request):
    try:
        location_data = request.data
        slug=None
        if 'location_image' in location_data and location_data['location_image']!=None:
            fmt, img_str = str(location_data['location_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            location_data['location_image'] = img_file

        if 'banner_image' in location_data and location_data['banner_image']!=None:
            fmt, img_str = str(location_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            location_data['banner_image'] = img_file
        
        # slug = slugify(location_data['locations_name'])
        suffix=1
        # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
        if Location.objects.filter(locations_name__exact=location_data['locations_name']).exists():
            count=Location.objects.filter(locations_name__exact=location_data['locations_name']).count()
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
                'code': status.HTTP_200_OK,
                'response': "Data created successfully",
                'data': serializer.data

            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not found",
                'error': serializer.errors
            })

    except Exception as e:
        return Response({
            'code':status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def complete_update(request, pk=None):
    try:
        id = pk
        location = Location.objects.get(id=id)
        location_data = request.data
        print(location_data)
        
        if ('location_image' in location_data and location_data['location_image']==None) and location.location_image!=None:
            print('hello')
            location_data.pop('location_image')
        if ('banner_image' in location_data and location_data['banner_image']==None) and location.banner_image!=None:
            print('hello2')
            location_data.pop('banner_image')
           
        print(location_data)
        if 'location_image' in location_data and location_data['location_image']!=None:
            fmt, img_str = str(location_data['location_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            location_data['location_image'] = img_file
        
        if 'banner_image' in location_data and location_data['banner_image']!=None:
            fmt, img_str = str(location_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            location_data['banner_image'] = img_file

            
        suffix=1
        # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
        if Location.objects.filter(locations_name__exact=location_data['locations_name']).exists():
            count=Location.objects.filter(locations_name__exact=location_data['locations_name']).count()
            print(count)
            suffix+=count
            print("yes")
            slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
        
        else:
            slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
                
        location_data['slug']=slug
        
        serializer = LocationSerializer(location, data=location_data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data updated successfully",
                'data': serializer.data

            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not found",
                'error': serializer.errors
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
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
        return Response({'code': status.HTTP_200_OK,'response': 'Data Deleted Successfully'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
