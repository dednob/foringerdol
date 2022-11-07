from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Event
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.utils.text import slugify

from django.core.files.base import ContentFile
from rest_framework import status



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_events(request, pk=None):
    id = pk
    try:
        if id is not None:
            event = Event.objects.get(id=id)
            serializer = EventReadSerializer(event)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })
        
        events = Event.objects.all()
        serializer = EventReadSerializer(events, many=True)
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
def events_by_location(request, locationid):
    try:
        locationid = locationid
        events = Event.objects.filter(location= locationid)
        serializer = EventReadSerializer(events, many=True)
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
@permission_classes([IsAuthenticated])
def create_event(request):
    try:
        event_data = request.data
        if 'event_image' in event_data and event_data['event_image']!=None:
            fmt, img_str = str(event_data['event_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            event_data['event_image'] = img_file
        
        if 'banner_image' in event_data and event_data['banner_image']!=None:
            fmt, img_str = str(event_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            event_data['banner_image'] = img_file

        slug = slugify(event_data['event_name'])
        suffix=1
        # slug = "%s-%s" % (slugify(location_data['locations_name']), suffix)
        if Event.objects.filter(event_name__exact=slug).exists():
            count=Event.objects.filter(event_name__exact=slug).count()
            print(count)
            suffix+=count
            print("yes")
            slug = "%s-%s" % (slugify(event_data['event_name']), suffix)
        
        else:
            slug = "%s-%s" % (slugify(event_data['event_name']), suffix)
                
        event_data['slug']=slug
        
        serializer = EventSerializer(data=event_data)
        print(serializer)
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
def complete_update_event(request, pk=None):
    id = pk
    try:
        event_data = request.data
        if 'event_image' in event_data:
            fmt, img_str = str(event_data['event_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            event_data['event_image'] = img_file
        
        if 'banner_image' in event_data:
            fmt, img_str = str(event_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            event_data['banner_image'] = img_file

        event =Event.objects.get(id=id)
        serializer = EventSerializer(event, data= event_data)
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
def partial_update_event(request, pk=None):
    id = pk
    event = Event.objects.get(pk=id)
    serializer = EventSerializer(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_event(request, pk=None):
    id = pk
    try: 
        event = Event.objects.get(pk=id)
        event.delete()
        return Response({'code': status.HTTP_200_OK,'msg': 'Data Deleted'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })


# Create your views here.

@api_view(['GET'])
def trending_event(request):
    try:
        events = Event.objects.filter(trending=True)
        serializer = EventReadSerializer(events, many=True)
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

