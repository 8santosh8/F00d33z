from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class User_Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=10,decimal_places=0)
    address = models.CharField(max_length=300)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pincode = models.DecimalField(max_digits=6,decimal_places=0)
    image = models.ImageField(default='default.png',upload_to='profile_pics')
    rest = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.User.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            desired_size = (300 ,300)
            img.thumbnail(desired_size)
            img.save(self.image.path)