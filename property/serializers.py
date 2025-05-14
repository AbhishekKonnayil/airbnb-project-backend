from rest_framework import serializers
from .models import Property


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'title', 'price_per_night', 'image_url')


class PropertiesDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('id', 'title', 'price_per_night', 'bedrooms',
                  'bathrooms', 'description', 'guests', 'landlord', 'image_url')
