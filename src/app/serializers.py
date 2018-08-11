from rest_framework import serializers

from app.models import Rides

class RidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rides
        fields = ('id', 'request_time', 'driver', 'customer', 'status')