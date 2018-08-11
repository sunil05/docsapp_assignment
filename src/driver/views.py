from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Rides
from driver.models import Driver
from django.db.models import Q
from app.serializers import RidesSerializer
import asyncio, time
import itertools
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_app(request):
    driver_id = request.GET.get('id', None)
    if driver_id:
        return render_to_response('driver.html', context={'driver_id':driver_id})
    return Response(400)

@api_view(['GET'])
def get_rides(request, driver_id):
    rides = Rides.objects.filter(Q(driver__id = driver_id)|Q(status='0')).order_by('-request_time')

    waiting = RidesSerializer(rides.filter(status='0'), many=True).data
    ongoing = RidesSerializer(rides.filter(status='1'), many=True).data
    completed = RidesSerializer(rides.filter(status='2'), many=True).data
    return Response(list(itertools.zip_longest(waiting, ongoing, completed, fillvalue='')))


@api_view(['GET'])
@csrf_exempt
def accept_request(request, driver_id, ride_id):
    if ride_id and driver_id:
        ride = Rides.objects.get(id = ride_id)
        driver = Driver.objects.get(id=driver_id)
        if ride and driver and ride.status=='0':
            ride.driver = driver
            ride.status = '1'
            ride.pickup_time = datetime.now()
            ride.save()
            print(time.time())
            mark_ride_complete(ride.id)
            print(time.time())

        return Response(200)

    return Response(400)

async def mark_ride_complete(ride_id):
    await asyncio.sleep(60)
    ride = Rides.objects.get(id=ride_id)
    ride.status = '2'
    ride.complete_time = datetime.now()
    ride.save()


