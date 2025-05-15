from rest_framework import serializers
from .models import Property
from useraccount.serializers import UserDetailSerializer


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'title', 'price_per_night', 'image_url')


class PropertiesDetailsSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True, many=False)

    class Meta:
        model = Property
        fields = ('id', 'title', 'price_per_night', 'bedrooms',
                  'bathrooms', 'description', 'guests', 'landlord', 'image_url')
