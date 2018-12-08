from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Order,Driver,userdet
from django.utils import timezone

# Create your views here.
def index1(request):
    return render(request,'gpstrack/index1.html')
def result(request):
    print("Request Object: {}".format(request.POST))
    driverid = request.POST.get('driverid1')
    if Driver.objects.filter(id=driverid):
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        Driver.objects.update(id=driverid,lat=lat,long=long, lastupdate=timezone.now())
        return HttpResponse("thank you for filling the form")
    else:
        return HttpResponse("check your id : ")
def getcurrloc(request):
  return render(request, 'gpstrack/index3.html')
def coord(request):
    return render(request, 'gpstrack/getpos.html')
def map(request):
    usID = "sandeep"
    order_id =userdet.objects.get(userid=usID).orderid
    driver_id = Order.objects.get(order=order_id).driver
    driv_id =str(driver_id)[-6:-1]
    time = Driver.objects.get(id=driv_id).lastupdate
    mapvalue={
        'lat':Driver.objects.get(id=driv_id).lat,
        'long':Driver.objects.get(id=driv_id).long,
        'time':time,
    }
    return render(request , 'gpstrack/maps.html',mapvalue)