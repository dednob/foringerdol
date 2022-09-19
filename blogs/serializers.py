from rest_framework import serializers

from blogs.models import Blog



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'story','blog_image']