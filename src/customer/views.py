from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import User
from driver.models import Driver
from app.models import Rides
import math
import json

# Create your views here.
DIS = lambda driver, rider: math.sqrt((int(driver.location_x) - int(rider.location_x))**2 + \
                                      (int(driver.location_y) - int(rider.location_y))**2)

def get_app(request):
    return render_to_response('customer.html', context={'customer_id': 'Set ID'})


@api_view(['GET'])
def request_cab(request):
    customer_id = request.GET.get('customer_id', None)
    location_x = request.GET.get('location_x', None)
    location_y = request.GET.get('location_y', None)
    if customer_id:
        usr, created = User.objects.get_or_create(userid=customer_id)
        usr.location_x = location_x
        usr.location_y = location_y
        usr.save()

        pending_req = Rides.objects.filter(status='0')
        if pending_req.count()<10:
            ride = Rides.objects.create(customer = usr, status='0')
            drivers = Driver.objects.all()
            nearest = []
            for obj in drivers:
                if len(nearest) < 3:
                    nearest.append((obj.id, DIS(usr, obj)))
                else:
                    away = max(nearest, key=lambda X: X[1])
                    if away[1] > DIS(usr, obj):
                        nearest.remove(away)
                        nearest.append((obj.id, DIS(usr, obj)))

            ride.nearest_driver = json.dumps(nearest)
            ride.save()
            return render_to_response('customer.html', context={'customer_id': customer_id, 'status':'ok'})
        else:
            return render_to_response('customer.html', context={'customer_id': customer_id, 'status': 'unavailable'})
    else:
        return Response(status=400)
