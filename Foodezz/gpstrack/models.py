from django.db import models
from Hotel import models as Hotelmodels

# Create your models here.
class Driver(models.Model):
    deliveryid=models.CharField(primary_key=True, max_length=12)#, default=1)
    restid=models.ForeignKey(Hotelmodels.RestaurantLog, on_delete=models.PROTECT)#, default=1)
    name = models.CharField(max_length=50)
    lat = models.FloatField(max_length=30)
    long = models.FloatField(max_length=30)
    lastupdate = models.DateTimeField()

    def __str__(self):
        return 'Driver: ' + self.name
