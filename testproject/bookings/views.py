from django.shortcuts import render
from django.http import HttpResponse
from .models import Custlog,Restaurantdetails,Orders

# Create your views here.

def loginorsignup(request):
    return render(request,'bookings/loginorsignup.html')

def login(request):
    return render(request,'bookings/login.html')

def signup(request):
    return render(request,'bookings/signup.html')

def loginsubmit(request):
    fullname=request.POST['fullname']
    password=request.POST['password']
    allfullname=Custlog.objects.all().values_list('fullname')
    allpassword=Custlog.objects.all().values_list('password')
    flag=2
    for i,j in allfullname,allpassword:
        if(i[0]==fullname):
            if(j[0]==password):
                flag=0
            elif(not flag==0):
                flag=1

    if(flag==0):
        return HttpResponse('You are logged in')
    elif(flag==1):
        return HttpResponse('password incorrect')
    else:
        return HttpResponse('username incorrect')

def signupsubmit(request):
    fullname=request.POST['fullname']
    password=request.POST['password']
    email=request.POST['email']
    Customer = Custlog.objects.create(fullname=fullname, email=email, password=password)
    return HttpResponse('you are signedup')