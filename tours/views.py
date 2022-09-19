from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Tour
from .serializers import TourSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTour(request, pk=None):
    id = pk
    if id is not None:
        tour = Tour.objects.get(id=id)
        serializer = TourSerializer(tour)
        return Response(serializer.data)
    tours = Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTour(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def completeUpdateTour(request, pk=None):
    id = pk
    tour = Tour.objects.get(id=id)
    serializer = TourSerializer(tour, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Complete Data Updated'})
    return Response(serializer.errors)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partialUpdateTour(request, pk=None):
    id = pk
    tour = Tour.objects.get(pk=id)
    serializer = TourSerializer(tour, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTour(request, pk=None):
    id = pk
    tour = Tour.objects.get(pk=id)
    tour.delete()
    return Response({'msg': 'Data Deleted'})
