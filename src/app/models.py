from django.db import models
from datetime import datetime


class Rides(models.Model):
    request_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[('0', 'wait'), ('1', 'ongoing'), ('2', 'completed')],  max_length=5)
    customer = models.ForeignKey('customer.User', null=False, on_delete=models.DO_NOTHING)
    driver = models.ForeignKey('driver.Driver', null=True, on_delete=models.DO_NOTHING )



#
# class RideHistory(models.Model):
#     pass

