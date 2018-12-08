from django.db import models


# Create your models here.
class Driver(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)
    lat = models.FloatField(max_length=30)
    long = models.FloatField(max_length=30)
    lastupdate = models.DateTimeField()

class Order(models.Model):
    order = models.CharField(max_length=150)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class userdet(models.Model):
    userid = models.CharField(max_length=30)
    orderid =models.CharField(max_length=30)