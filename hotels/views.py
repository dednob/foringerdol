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
from rest_framework import status



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_hotel(request, pk=None):
    try:
        id = pk
        if id is not None:
            hotel = Hotel.objects.get(id=id)
            serializer = HotelReadSerializer(hotel)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })
        hotels = Hotel.objects.all()
        serializer = HotelReadSerializer(hotels, many=True)
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
def hotels_by_location(request, locationid):

    locationid = locationid
    try:
        hotels = Hotel.objects.filter(location= locationid)
        serializer = HotelReadSerializer(hotels, many=True)
        return Response(serializer.data)
    
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_hotel(request):
    try:
        hotel_data = request.data
        if 'hotel_image' in hotel_data and hotel_data['hotel_image']!=None:
            fmt, img_str = str(hotel_data['hotel_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            hotel_data['hotel_image'] = img_file

        if 'banner_image' in hotel_data and hotel_data['banner_image']!=None:
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
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def complete_update_hotel(request, pk=None):
    try:
        id = pk
        hotel = Hotel.objects.get(id=id)
        hotel_data = request.data
        
        
        if ('hotel_image' in hotel_data and hotel_data['hotel_image']==None) and hotel.hotel_image!=None:
            
            hotel_data.pop('hotel_image')

        if ('banner_image' in hotel_data and hotel_data['banner_image']==None) and hotel.banner_image!=None:
            
            hotel_data.pop('banner_image')
        
        if 'hotel_image' in hotel_data and hotel_data['hotel_image']!=None:
            fmt, img_str = str(hotel_data['hotel_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            hotel_data['hotel_image'] = img_file

        if 'banner_image' in hotel_data and hotel_data['banner_image']!=None:
            fmt, img_str = str(hotel_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            hotel_data['banner_image'] = img_file
            
        

           

        serializer = HotelSerializer(hotel, data=request.data)
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
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


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
    try:
        hotel = Hotel.objects.get(pk=id)
        hotel.delete()
        return Response({'code':status.HTTP_200_OK,'msg': 'Hotel data Deleted'})
        
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })

@api_view(['GET'])
def popular_hotels(request):
    try:
        events = Hotel.objects.filter(popular=True)
        serializer = HotelReadSerializer(events, many=True)
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
