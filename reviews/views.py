from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET'])
def review_list(request):
    try:
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many = True)
        return Response(serializer.data)
    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
    

@api_view(['POST'])
def create_review(request):
    try:
        serializer = ReviewSerializer(data = request.data)
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
def update_review(request, pk):
    try:
        rev_data = request.data
        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(review, data = rev_data, partial = True)
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

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_review(request,pk):
    try:
        review = Review.objects.get(id=pk)
        review.delete()
        return Response({'code': request.status.HTTP_200_OK,'msg': 'Data Deleted'})
    except Exception as e:
        return Response({
            'code': request.status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })