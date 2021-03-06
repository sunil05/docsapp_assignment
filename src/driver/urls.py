"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from driver.views import get_app, accept_request, get_rides, complete_ride

urlpatterns = [
    path('', get_app),
    path('<int:driver_id>/accept_request/<int:ride_id>', accept_request),
    path('<int:driver_id>/complete_ride/<int:ride_id>', complete_ride),
    path('<int:driver_id>/get_rides', get_rides)

]
