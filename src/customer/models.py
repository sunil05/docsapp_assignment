from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=100)
    location_x = models.IntegerField(default=0)
    location_y = models.IntegerField(default=0)
