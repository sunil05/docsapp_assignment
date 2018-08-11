from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import User
from app.models import Rides

# Create your views here.
def get_app(request):
    return render_to_response('customer.html', context={'customer_id': 'Set ID'})


@api_view(['GET'])
def request_cab(request):
    customer_id = request.GET.get('customer_id', None)
    if customer_id:
        usr, created = User.objects.get_or_create(userid=customer_id)
        ride = Rides.objects.create(customer = usr, status='0')
        return render_to_response('customer.html', context={'customer_id': customer_id})
    else:
        return Response(status=400)
