from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#from gpstrack.models import Driver

# Create your models here.

class CustomerLog(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=150, unique=True)
    password=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    pincode = models.CharField(max_length=6)


class RestaurantLog(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    street=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    pincode=models.CharField(max_length=6)
    restimage = models.ImageField(upload_to='restaurant/rest', blank=True)

class RestaurantItems(models.Model):
    restaurantid=models.ForeignKey(RestaurantLog,on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
    category=models.CharField(max_length=150)
    price=models.CharField(max_length=6)
    availability=models.CharField(max_length=6)
    foodimage=models.ImageField(upload_to='restaurant/food',blank=True)

class Orders(models.Model):
    orderid = models.CharField(max_length=12)
    customerid=models.ForeignKey(User, on_delete=models.PROTECT)
    restaurantid=models.ForeignKey(RestaurantLog, on_delete=models.PROTECT)
    deliveryid=models.CharField(max_length=12)

    #driverid = models.ForeignKey(Driver, on_delete=models.PROTECT)

    foodname=models.CharField(max_length=150)
    quantity=models.CharField(max_length=4)
    price=models.CharField(max_length=5)
    date=models.DateTimeField(default=datetime.now, blank=True)
    status=models.CharField(max_length=150)

class CustomerCart(models.Model):
    customerid=models.ForeignKey(User, on_delete=models.PROTECT)
    restaurantid = models.ForeignKey(RestaurantLog, on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)
    status=models.CharField(max_length=50,default='buylater')

class Feedback(models.Model):
    rate=models.IntegerField()
    suggestion=models.CharField(max_length=200)