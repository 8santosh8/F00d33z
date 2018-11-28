from django.db import models
from django.contrib.auth.models import User

class User_Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=10,decimal_places=0)
    address = models.CharField(max_length=300)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pincode = models.DecimalField(max_digits=6,decimal_places=0)

    def __str__(self):
        return self.User.username