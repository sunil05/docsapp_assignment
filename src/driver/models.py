from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    location_x = models.IntegerField(default=0)
    location_y = models.IntegerField(default=0)