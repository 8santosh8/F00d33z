from django.shortcuts import render
from . import decorators
from .models import RestaurantItems,RestaurantLog, Orders

@decorators.HotelUser
def Home(request):
    return render(request,'Hotel/Home.html',)

@decorators.HotelUser
def ItemView(request):
    rest = RestaurantLog.objects.filter(manager=request.user).first()
    restaurantItems = RestaurantItems.objects.filter(restaurantid=rest)
    order = Orders.objects.filter(restaurantid=rest, status='SentToRestaurant')
    inprogress = Orders.objects.filter(restaurantid=rest, status='OutForDelivery')
    data = {"food": restaurantItems, "rest": rest, "orders": order, "inpro":inprogress}
    return render(request,'Hotel/ItemView.html',data)

@decorators.HotelUser
def Update(request):
    if request.method == 'POSt':
        if request.POST['submit'] == 'Update':
            pass
        elif request.POST['submit'] == 'Add New Item':
            pass
        return render(request,'Hotel/ItmeUpdate',)
    else:
        return redirect('Hotel-ItemView')
