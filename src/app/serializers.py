from rest_framework import serializers
from customer.models import User
from app.models import Rides

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userid', )

class RidesSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    class Meta:
        model = Rides
        fields = ('id', 'request_time', 'pickup_time', 'complete_time', 'driver', 'customer', 'status', 'nearest_driver')