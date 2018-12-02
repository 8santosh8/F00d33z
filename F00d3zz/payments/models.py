from django.db import models

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

class RestaurantItems(models.Model):
    restaurantid=models.ForeignKey(RestaurantLog,on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
    price=models.CharField(max_length=6)
    availability=models.CharField(max_length=6)

class Orders(models.Model):
    orderid = models.CharField(max_length=12)
    customerid=models.ForeignKey(CustomerLog, on_delete=models.PROTECT)
    restaurantid=models.ForeignKey(RestaurantLog, on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)
    quantity=models.CharField(max_length=4)
    date=models.DateTimeField
    status=models.CharField(max_length=150)

class CustomerCart(models.Model):
    customerid=models.ForeignKey(CustomerLog, on_delete=models.PROTECT)
    restaurantid = models.ForeignKey(RestaurantLog, on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)
    status=models.CharField(max_length=50,default='buylater')