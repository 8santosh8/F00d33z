from django.contrib import admin

# Register your models here.

from .models import Custlog,Restaurantdetails,Orders

admin.site.register(Custlog)
admin.site.register(Restaurantdetails)
admin.site.register(Orders)
