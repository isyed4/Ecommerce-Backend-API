from rest_framework import serializers
from ..models.electronics import Electronic


class ElectronicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic
        fields = ('id', 'name', 'price', 'rating', 'image_url')
