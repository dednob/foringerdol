from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Package
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import base64
from django.utils.text import slugify

from django.core.files.base import ContentFile
from rest_framework import status


@api_view(['GET'])
def get_packages(request, slug=None):
    slug = slug
    try:
        if slug is not None:
            package = Package.objects.get(slug=slug)
            serializer = PackageReadSerializer(package)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Received data Successfully",
                'data': serializer.data

            })

        packages = Package.objects.all()
        serializer = PackageReadSerializer(packages, many=True)
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
def packages_by_event(request, eventid):
    try:
        eventid = eventid
        packages = Package.objects.filter(event=eventid)
        serializer = PackageReadSerializer(packages, many=True)
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
def create_package(request):
    try:
        package_data = request.data
        if 'package_image' in package_data and package_data['package_image']!=None:
            fmt, img_str = str(package_data['package_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            package_data['package_image'] = img_file

        if 'banner_image' in package_data and package_data['banner_image']!=None:
            fmt, img_str = str(package_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            package_data['banner_image'] = img_file

        suffix=1
        if Package.objects.filter(package_name__exact=package_data['package_name']).exists():
            count=Package.objects.filter(package_name__exact=package_data['package_name']).count()
            suffix+=count
            slug = "%s-%s" % (slugify(package_data['package_name']), suffix)

        else:
            slug = "%s-%s" % (slugify(package_data['package_name']), suffix)

        package_data['slug']=slug

        serializer = PackageSerializer(data=package_data)
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
def complete_update_package(request, pk=None):

    try:
        id = pk
        package = Package.objects.get(id=id)
        package_data = request.data

        if ('package_image' in package_data and package_data['package_image']==None) and package.package_image!=None:
            package_data.pop('package_image')
        if ('banner_image' in package_data and package_data['banner_image']==None) and package.banner_image!=None:
            package_data.pop('banner_image')

        if 'package_image' in package_data and package_data['package_image']!=None:
            fmt, img_str = str(package_data['package_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            package_data['package_image'] = img_file

        if 'banner_image' in package_data and package_data['banner_image']!=None:
            fmt, img_str = str(package_data['banner_image']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            package_data['banner_image'] = img_file

        suffix=1
        if Package.objects.filter(package_name__exact=package_data['package_name']).exists():
            count=Package.objects.filter(package_name__exact=package_data['package_name']).count()
            suffix+=count
            slug = "%s-%s" % (slugify(package_data['package_name']), suffix)

        else:
            slug = "%s-%s" % (slugify(package_data['package_name']), suffix)

        package_data['slug']=slug

        serializer = PackageSerializer(package, data=package_data)
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


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def partial_update_package(request, pk=None):
    id = pk
    package = Package.objects.get(pk=id)
    serializer = PackageSerializer(package, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_package(request, pk=None):
    id = pk
    try:
        package = Package.objects.get(pk=id)
        package.delete()
        return Response({'code': status.HTTP_200_OK,'response': 'Data Deleted Successfully'})

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'response': "Data not found",
            'error': str(e)
        })
