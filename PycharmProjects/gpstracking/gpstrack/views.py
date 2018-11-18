from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Order,Driver
from django.utils import timezone
import json
# Create your views here.
def index1(request):
    return render(request , 'gpstrack/index1.html')
def result(request):
    print("Request Object: {}".format(request.POST))
    driverid = request.POST.get('driverid1')
    location = request.POST.get('location')
    if Driver.objects.get(id=driverid):
        driv = Driver.objects.get(id=driverid)
        driv.currlocation = location
        driv.lastupdate=timezone.now()
        driv.save()
    else:
        Driver.objects.create(id=driverid, currlocation= location, lastupdate=timezone.now())
    return HttpResponse("thank you for filling the form")

def getcurrloc(request):
    loc=" "
    if request.method == 'POST':
        currdriver = get_object_or_404(Driver, id=request.POST.get('driverid'))
        loc = currdriver.currlocation
    context = {
        'location' : loc
    }
    return render(request, 'gpstrack/index3.html', context)
def map(request):
    driverid= request.POST.get('driverid')
    mapvalue = Driver.objects.get(id=driverid).currlocation
    return render(request , 'gpstrack/maps.html', {'json_string' : json.dumps(mapvalue)})