from django.db import models


# Create your models here.
class Driver(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)
    currlocation = models.CharField(max_length=150)
    lastupdate = models.DateTimeField()

class Order(models.Model):
    order = models.CharField(max_length=150)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)