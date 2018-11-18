from django.shortcuts import render
from django.http import HttpResponse
from .models import UserLog,EquationLog

# Create your views here.

def index(request):
    return render(request,'force/index.html')

def result(request):
    fullname=request.POST['fullname']
    email=request.POST['email']

    userlog = UserLog.objects.create
    m1=request.POST['m1']
    x1=request.POST['x1']
    m2=request.POST['m2']
    x2=request.POST['x2']
    com=(float(m1) * float(x1) + float(m2) * float(x2)) / (float(x1)+float(x2))
    context = {
        "com":com
    }
    return render(request,'force/result.html',context=context)