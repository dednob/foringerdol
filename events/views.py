from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64

from django.core.files.base import ContentFile


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEvent(request, pk=None):
    id = pk
    if id is not None:
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def completeUpdateEvent(request, pk=None):
    id = pk
    event =Event.objects.get(id=id)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Complete Data Updated'})
    return Response(serializer.errors)


@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def partialUpdateEvent(request, pk=None):
    id = pk
    event = Event.objects.get(pk=id)
    serializer = EventSerializer(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteEvent(request, pk=None):
    id = pk
    event = Event.objects.get(pk=id)
    event.delete()
    return Response({'msg': 'Data Deleted'})
from django.shortcuts import render

# Create your views here.
