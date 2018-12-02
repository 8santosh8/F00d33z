from django.contrib import admin

# Register your models here.

from .models import UserLog,EquationLog

admin.site.register(UserLog)
admin.site.register(EquationLog)
