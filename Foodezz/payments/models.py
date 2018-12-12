from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from Hotel import models as Hotelmodels
#from gpstrack.models import Driver

class Orders(models.Model):
    orderid = models.CharField(max_length=12)
    customerid=models.ForeignKey(User, on_delete=models.PROTECT)
    restaurantid=models.ForeignKey(Hotelmodels.RestaurantLog, on_delete=models.PROTECT)
    deliveryid=models.CharField(max_length=12)

    #driverid = models.ForeignKey(Driver, on_delete=models.PROTECT)

    foodname=models.CharField(max_length=150)
    quantity=models.CharField(max_length=4)
    price=models.CharField(max_length=5)
    date=models.DateTimeField(default=datetime.now, blank=True)
    status=models.CharField(max_length=150)

    def __str__(self):
        return self.foodname + ' ' + self.orderid

class CustomerCart(models.Model):
    customerid=models.ForeignKey(User, on_delete=models.PROTECT)
    restaurantid = models.ForeignKey(Hotelmodels.RestaurantLog, on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)
    status=models.CharField(max_length=50,default='buylater')

    def __str__(self):
        return self.customerid
