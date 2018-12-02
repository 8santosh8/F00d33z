from django.contrib import admin

# Register your models here.

from .models import CustomerLog,RestaurantLog,RestaurantItems,CustomerCart,Orders

admin.site.register(CustomerLog)
admin.site.register(RestaurantLog)
admin.site.register(RestaurantItems)
admin.site.register(CustomerCart)
admin.site.register(Orders)