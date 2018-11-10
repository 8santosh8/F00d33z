from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomerLog,RestaurantLog,CustomerCart,RestaurantItems,Orders

# Create your views here.

def restaurantselection(request):
    return render(request, 'payment/../templates/payments/restaurant.html')

def foodselection(request):
    return HttpResponse('yoyoyoyo')