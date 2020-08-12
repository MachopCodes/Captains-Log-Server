from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from types import SimpleNamespace
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from ..models.tide import Tide
from ..models.trip import Trip
from ..serializers import TideSerializer

class Tide(generics.ListCreateAPIView):
    serializer_class = TideSerializer
    def post(self, request):
        """Create request"""
        trip = get_object_or_404(Trip, pk=request.data[0])
        tideArray = request.data[1]['extremes']
        for tide in tideArray:
            tide['trip'] = trip.id
            dotTide = SimpleNamespace(**tide)
            ts = TideSerializer(data=tide)
            if ts.is_valid():
                m = ts.save()
                ts = trip.tide_set.create(timestamp=dotTide.timestamp, datetime=dotTide.datetime, height=dotTide.height, state=dotTide.state)
                return Response(ts.data, status=status.HTTP_201_CREATED)
            else:
                return Response(ts.errors, status=status.HTTP_400_BAD_REQUEST)
