from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.electronics import Electronics
from ..serializers.electronics import ElectronicsSerializer
from django.shortcuts import get_object_or_404


class ElectronicsView(APIView):
    def get(self, request):
        electronics = Electronics.objects.all()
        data = ElectronicsSerializer(electronics, many=True).data
        return Response(data)
    
    def post(self, request):
        electronic = ElectronicsSerializer(data=request.data)
        if electronic.is_valid():
            electronic.save()
            return Response(electronic.data, status=status.HTTP_201_CREATED)
        else:
            return Response(electronic.errors, status.HTTP_400_BAD_REQUEST)


class ElectronicView(APIView):
    def get(self, request, pk):
        electronic = get_object_or_404(Electronics, pk=pk)
        data = ElectronicsSerializer(electronic).data
        return Response(data)

    def delete(self, request, pk):
        electronic = get_object_or_404(Electronics, pk=pk)
        electronic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        electronic = get_object_or_404(Electronics, pk=pk)
        updated_electronic = ElectronicsSerializer(electronic, data=request.data)
        if updated_electronic.is_valid():
            updated_electronic.save()
            return Response(updated_electronic.data)
        else:
            return Response(updated_electronic.errors, status=status.HTTP_400_BAD_REQUEST)



