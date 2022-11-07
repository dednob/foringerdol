from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Tour
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile
from django.utils.text import slugify


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_tour(request, pk=None):
    id = pk
    try:
        if id is not None:
            tour = Tour.objects.get(id=id)
            serializer = TourReadSerializer(tour)
            return Response({
                'code': request.status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })
        tours = Tour.objects.all()
        serializer = TourReadSerializer(tours, many=True)
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
def tours_by_location(request, locationid):
    try:
        locationid = locationid
        tours = Tour.objects.filter(location= locationid)
        serializer = TourReadSerializer(tours, many=True)
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
def create_tour(request):
    try:
        tour_data = request.data
        if 'tour_image' in tour_data and tour_data['tour_image']!=None:
            fmt, img_str = str(tour_data['tour_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            tour_data['tour_image'] = img_file
        
        if 'banner_image' in tour_data and tour_data['banner_image']!=None:
            fmt, img_str = str(tour_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            tour_data['banner_image'] = img_file

        slug = slugify(tour_data['tour_name'])
        suffix=1
        # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
        if Tour.objects.filter(tour_name__exact=slug).exists():
            count=Tour.objects.filter(tour_name__exact=slug).count()
            print(count)
            suffix+=count
            print("yes")
            slug = "%s-%s" % (slugify(tour_data['tour_name']), suffix)
        
        else:
            slug = "%s-%s" % (slugify(tour_data['tour_name']), suffix)
                
        tour_data['slug']=slug

        serializer = TourSerializer(data=tour_data)
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
def complete_update_tour(request, pk=None):
    try:

        tour_data = request.data
        if 'tour_image' in tour_data:
            fmt, img_str = str(tour_data['tour_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            tour_data['tour_image'] = img_file

        if 'banner_image' in tour_data:
            fmt, img_str = str(tour_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            tour_data['banner_image'] = img_file

        id = pk
        tour = Tour.objects.get(id=id)
        serializer = TourSerializer(tour, data=tour_data)
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
def partial_update_tour(request, pk=None):
    id = pk
    tour = Tour.objects.get(pk=id)
    serializer = TourSerializer(tour, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_tour(request, pk=None):
    try:
        id = pk
        tour = Tour.objects.get(pk=id)
        tour.delete()
        return Response({'code': request.status.HTTP_200_OK,'msg': 'Data Deleted'})
    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
