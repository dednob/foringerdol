from django.shortcuts import render
from .models import Booking
from events.models import Event
from hotels.models import Hotel
from locations.models import Location

from .serializers import BookingSerializer
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile
from django.utils.text import slugify
from rest_framework import status

# Create your views here.

# Create, Delete, Get , Toggle

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_list(request):
    try:
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many = True)
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
@permission_classes([IsAuthenticated])
def get_booking_detail(request, pk):
    try:
        if pk is not None:
            booking = Booking.objects.get(id=pk)
            serializer = BookingSerializer(booking)
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
def create_booking(request):
    try:
        booking_data = request.data
        
        serializer = BookingSerializer(data = booking_data, partial = True)
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
# @permission_classes([IsAuthenticated])
def update_blog(request, pk):
    try: 
        id = pk
        booking = Booking.objects.get(id = id)
        booking_data = request.data
        

        serializer = BookingSerializer(booking, data = booking_data, partial = True)
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
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_booking(request,pk):
    booking = Booking.objects.get(id=pk)
    try:
        booking.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'response': "Data deleted successfully",

        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def toggle_payment_status(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        booking.payment_status = not booking.payment_status
        booking.save()
        serializer = BookingSerializer(booking)
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