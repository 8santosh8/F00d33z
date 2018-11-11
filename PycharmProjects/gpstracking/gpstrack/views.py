from django.shortcuts import render
from django.http import HttpResponse
from .models import orderscarrying,presentlocation
# Create your views here.
def index1(request):
    return render(request , 'gpstrack/index1.html')
def index2(request):
    return render(request , 'gpstrack/index2.html')
def results(request):
    print("Request Object: {}".format(request.POST))
    driverid = request.POST['driverid']
    location = request.POst['location']
    presentlocation = presentlocation.objects.create(driverid = driverid ,location = location)
    orderid =request.POST['orderid']
    