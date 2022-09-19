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
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)