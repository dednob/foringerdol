from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tour
from .serializers import TourSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


@api_view(['GET'])
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
def createTour(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def completeUpdateTour(request, pk=None):
    id = pk
    tour = Tour.objects.get(id=id)
    serializer = TourSerializer(tour, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Complete Data Updated'})
    return Response(serializer.errors)


@api_view(['PATCH'])
def partialUpdateTour(request, pk=None):
    id = pk
    tour = Tour.objects.get(pk=id)
    serializer = TourSerializer(tour, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
def deleteTour(request, pk=None):
    id = pk
    tour = Tour.objects.get(pk=id)
    tour.delete()
    return Response({'msg': 'Data Deleted'})
