from django.db import models

# Create your models here.
class presentlocation:
    driverid = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
class orderscarrying:
    orderid = models.CharField(max_length=150)
    driverid = models.CharField(max_length=150)
