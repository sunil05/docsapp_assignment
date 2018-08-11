from django.shortcuts import render_to_response
from app.serializers import RidesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_dashboard(request):
    return render_to_response('dashboard.html')

@api_view(['GET'])
def get_rides(request):
    serialized_data = RidesSerializer()
    return Response(data=serialized_data.data)