from django.db import models

# Create your models here.

class UserLog(models.Model):
    userlogid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

class EquationLog(models.Model):
    mass1 = models.FloatField(null=False)
    position1 = models.FloatField(null=False)
    mass2 = models.FloatField(null=False)
    position2 = models.FloatField(null=False)
    com = models.FloatField(null=False)
    userlogid = models.ForeignKey(UserLog, on_delete=models.PROTECT)