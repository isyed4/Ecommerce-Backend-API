from rest_framework import serializers
from ..models.electronics import Electronics


class ElectronicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronics
        fields = ('id', 'name', 'price', 'rating')
