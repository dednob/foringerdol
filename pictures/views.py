
from .models import Pictures
from .serializers import PicturesSerializer
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import base64
from django.core.files.base import ContentFile
from django.utils.text import slugify
from rest_framework import status



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_pictures(request):
    try:
        picture = Pictures.objects.last()
        serializer = PicturesSerializer(picture)
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
def update_picture(request):
    try:
        picture_data = request.data
        print(picture_data)
        picture = Pictures.objects.last()
        print(picture)
        if picture == None:
            print(picture_data)

            if 'header' in picture_data and picture_data['header']!=None:
                fmt, img_str = str(picture_data['header']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['header'] = img_file
            
            if 'promotionOne' in picture_data and picture_data['promotionOne']!=None:
                fmt, img_str = str(picture_data['promotionOne']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['promotionOne'] = img_file

            if 'promotionTwo' in picture_data and picture_data['promotionTwo']!=None:
                fmt, img_str = str(picture_data['promotionTwo']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['promotionTwo'] = img_file

            if 'footer' in picture_data and picture_data['footer']!=None:
                fmt, img_str = str(picture_data['footer']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['footer'] = img_file

            serializer = PicturesSerializer(data = picture_data, partial = True)
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

        else:
            print("Ami Running")

            if ('header' in picture_data and picture_data['header']==None) and picture.header!=None:
            
                picture_data.pop('header')

            if ('promotionOne' in picture_data and picture_data['promotionOne']==None) and picture.promotionOne!=None:
            
                picture_data.pop('promotionOne')

            if ('promotionTwo' in picture_data and picture_data['promotionTwo']==None) and picture.promotionTwo!=None:
            
                picture_data.pop('promotionTwo')
            
            if ('footer' in picture_data and picture_data['footer']==None) and picture.footer!=None:
            
                picture_data.pop('footer')



            if 'header' in picture_data and picture_data['header']!=None:
                fmt, img_str = str(picture_data['header']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['header'] = img_file
            
            if 'promotionOne' in picture_data and picture_data['promotionOne']!=None:
                fmt, img_str = str(picture_data['promotionOne']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['promotionOne'] = img_file

            if 'promotionTwo' in picture_data and picture_data['promotionTwo']!=None:
                fmt, img_str = str(picture_data['promotionTwo']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['promotionTwo'] = img_file

            if 'footer' in picture_data and picture_data['footer']!=None:
                fmt, img_str = str(picture_data['footer']).split(';base64,')
                ext = fmt.split('/')[-1]
                img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
                picture_data['footer'] = img_file

            serializer = PicturesSerializer(picture, data = picture_data, partial = True)
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