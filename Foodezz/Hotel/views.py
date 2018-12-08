from django.shortcuts import render
from . import decorators

@decorators.HotelUser
def Home(request):
    return render(request,'Hotel/Home.html',)
