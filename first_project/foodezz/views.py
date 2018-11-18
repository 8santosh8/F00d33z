from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'foodezz/home1.html')

def cart(request):
    return render(request,'foodezz/cart.html')
