from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from ..models.coor_pair import CoorPair
from ..serializers import CoordSerializer

class Coords(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, key):
        """Show request"""
        coords = CoorPair.objects.filter(key=key)
        data = CoordSerializer(coords[0]).data
        return Response(data)
# put data in the response
