from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.trip import Trip
from ..serializers import TripSerializer

class Trips(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        """Index request"""
        trips = Trip.objects.filter(owner=request.user.id)
        data = TripSerializer(trips, many=True).data
        return Response(data)

    serializer_class = TripSerializer
    def post(self, request):
        """Create request"""
        request.data['trip']['owner'] = request.user.id
        trip = TripSerializer(data=request.data['trip'])
        if trip.is_valid():
            m = trip.save()
            return Response(trip.data, status=status.HTTP_201_CREATED)
        else:
            return Response(trip.errors, status=status.HTTP_400_BAD_REQUEST)

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        trip = get_object_or_404(Trip, pk=pk)
        data = TripSerializer(trip).data
        # Only want to show owned trips?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this trip')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        trip = get_object_or_404(Trip, pk=pk)
        if not request.user.id == trip.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this trip')
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        trip = get_object_or_404(Trip, pk=pk)
        if not request.user.id == trip.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this trip')
        request.data['trip']['owner'] = request.user.id
        ms = TripSerializer(trip, data=request.data['trip'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
