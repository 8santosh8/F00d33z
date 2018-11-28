from django.db import models

# Create your models here.

class Custlog(models.Model):
    custid=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)


class Restaurantdetails(models.Model):
    restaurantid=models.AutoField(primary_key=True)
    restaurantname=models.CharField(max_length=150)
    street=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    pincode=models.CharField(max_length=6)

class Orders(models.Model):
    custid=models.ForeignKey(Custlog, on_delete=models.PROTECT)
    restaurantid=models.ForeignKey(Restaurantdetails, on_delete=models.PROTECT)
    orderid=models.CharField(max_length=12)
    item=models.CharField(max_length=5)
    quantity=models.CharField(max_length=4)

class CustomerCart(models.Model):
    custid=models.ForeignKey(Custlog, on_delete=models.PROTECT)
    restaurantid = models.ForeignKey(Restaurantdetails, on_delete=models.PROTECT)
    foodname=models.CharField(max_length=150)