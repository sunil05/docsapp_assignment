from django.db import models
from datetime import datetime
from customer.models import User
from driver.models import Driver


class Rides(models.Model):
    request_id = models.CharField(max_length=50)
    request_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[('0', 'wait'), ('1', 'ongoing'), ('2', 'completed')])
    customer_id = models.ForeignKey('customer.User', null=False, on_delete=models.DO_NOTHING)
    driver_id = models.ForeignKey('driver.Driver', null=True, on_delete=models.DO_NOTHING )



#
# class RideHistory(models.Model):
#     pass

