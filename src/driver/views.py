from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Rides
from driver.models import Driver
from django.db.models import Q
from app.serializers import RidesSerializer

# Create your views here.
def get_app():
    return render_to_response('driver.html', context={})

@api_view(['GET'])
def get_rides(request, driver_id):
    response = {'waiting':[], 'ongoing': [], 'completed': []}
    rides = Rides.objects.filter(Q(driver_id__id = driver_id)|Q(status='0')).order_by('-request_time')

    response['waiting'].extend(RidesSerializer(rides.filter(status='0'), many=True).data)
    response['ongoing'].extend(RidesSerializer(rides.filter(status='1'), many=True).data)
    response['completed'].extend(RidesSerializer(rides.filter(status='2'), many=True).data)
    return Response(response)


@api_view(['POST'])
def accept_request(request):
    ride_id = request.data.get('ride_id', None)
    driver_id = request.data.get('driver_id', None)
    if ride_id and driver_id:
        ride = Rides.objects.get(id = ride_id)
        driver = Driver.objects.get(id=driver_id)
        if ride and driver and ride.status=='0':
            ride.driver = driver
            ride.status = '1'
            ride.save()
            return Response(200)

    return Response(400)


