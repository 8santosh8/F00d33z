from django.contrib import admin
from.models import Driver, Order
from django.contrib.auth.models import Group,User


admin.site.site_header = 'F00d3zZ'
admin.site.register(Order)
admin.site.register(Driver)


admin.site.unregister(Group)
admin.site.unregister(User)