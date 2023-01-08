from rest_framework import serializers

from pictures.models import Pictures


class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = '__all__'
