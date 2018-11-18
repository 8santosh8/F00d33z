from django.shortcuts import render

def Home(request):
    return render(request,'Home/Home.html')

def Cart(request):
    return render(request,'Home/Cart.html')
