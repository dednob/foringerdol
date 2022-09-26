from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def blog_list(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many = True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    blog_data = request.data
    if 'blog_image' in blog_data:
        fmt, img_str = str(blog_data['blog_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        blog_data['blog_image'] = img_file
    
    if 'banner_image' in blog_data:
        fmt, img_str = str(blog_data['banner_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        blog_data['banner_image'] = img_file

    serializer = BlogSerializer(data = blog_data)
    if serializer.is_valid():
        serializer.save()    
        return Response(serializer.data)
    

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_blog(request, pk):
    blog_data = request.data
    if 'blog_image' in blog_data:
        fmt, img_str = str(blog_data['blog_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        blog_data['blog_image'] = img_file
    
    if 'banner_image' in blog_data:
        fmt, img_str = str(blog_data['banner_image']).split(';base64,')
        ext = fmt.split('/')[-1]
        img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
        blog_data['banner_image'] = img_file

    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, data = blog_data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog(request,pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return Response('Deleted')
    
    