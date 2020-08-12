from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.trip import Trip
from .models.user import User
from .models.coor_pair import CoorPair
from .models.tide import Tide

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'launchDate', 'latitude', 'longitude', 'city', 'state', 'owner') 

class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoorPair
        fields = '__all__'


class TideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tide
        fields = ('timestamp', 'datetime', 'height', 'state', 'trip')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
