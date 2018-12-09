from django.db import models
from payments.models import RestaurantLog

# Create your models here.
class Driver(models.Model):
    deliveryid=models.CharField(primary_key=True, max_length=12)#, default=1)
    restid=models.ForeignKey(RestaurantLog, on_delete=models.PROTECT)#, default=1)
    name = models.CharField(max_length=50)
    lat = models.FloatField(max_length=30)
    long = models.FloatField(max_length=30)
    lastupdate = models.DateTimeField()
#
# class Order(models.Model):
#     order = models.CharField(max_length=150)
#     driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
#
# class userdet(models.Model):
#     userid = models.CharField(max_length=30)
#     orderid =models.CharField(max_length=30)