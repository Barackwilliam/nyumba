from rest_framework import serializers
from .models import Property, PropertyLocation

class PropertyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyLocation
        fields = ['lat', 'lon']

    


class PropertySerializer(serializers.ModelSerializer):
    location = PropertyLocationSerializer()

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'price', 'status', 'p_status', 
                  'property_type', 'region', 'district', 'ward', 'business_phone', 
                  'bedrooms', 'bathrooms', 'house_size', 'nearby', 'image', 'location']
