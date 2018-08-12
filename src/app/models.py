from django.db import models
from datetime import datetime


class Rides(models.Model):
    request_time = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateTimeField(null=True)
    complete_time = models.DateTimeField(null=True)
    status = models.CharField(choices=[('0', 'wait'), ('1', 'ongoing'), ('2', 'completed')],  max_length=5)
    customer = models.ForeignKey('customer.User', null=False, on_delete=models.DO_NOTHING)
    driver = models.ForeignKey('driver.Driver', null=True, on_delete=models.DO_NOTHING )
    nearest_driver = models.CharField(max_length=500, default='[]')


#
# class RideHistory(models.Model):
#     pass

