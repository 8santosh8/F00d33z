from django.shortcuts import render
from . import decorators
from .models import RestaurantItems,RestaurantLog, Orders
from django.shortcuts import redirect
from django.contrib import messages

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
    if request.method == 'POST':
        if request.POST['submit'] == 'Update':
            rest = RestaurantLog.objects.filter(manager=request.user).first()
            items = RestaurantItems.objects.filter(restaurantid=rest)
            for item in items:
                foodname = item.foodname
                price = request.POST[foodname+'_price']
                availability=request.POST[foodname+'_availability']
                RestaurantItems.objects.filter(restaurantid=rest_id, foodname=foodname).update(price=price,availability=availability)
            return redirect('Hotel-ItemView')

        elif request.POST['submit'] == 'Add New Item':
            rest = RestaurantLog.objects.filter(manager=request.user).first()
            return render(request,'Hotel/AddItem.html',{'rest':rest.name})

        else:
            foodname = request.POST['foodname']
            rest = RestaurantLog.objects.filter(manager=request.user).first()
            RestaurantItems.objects.filter(restaurantid=rest,foodname=foodname).delete()
            return redirect('Hotel-ItemView')

    else:
        return redirect('Hotel-ItemView')


def AddItem(request):
    if request.method == 'POST':
        rest = RestaurantLog.objects.filter(manager=request.user).first()
        foodname=request.POST['foodname']
        type=request.POST['type']
        category=request.POST['category']
        price=request.POST['price']
        availability=request.POST['availability']
        foodimage=request.FILES['foodimage']
        if RestaurantItems.objects.filter(foodname=foodname):
            messages.error(request,f'Same foodname exists try creating with other food name.')

        else:
            RestaurantItems.objects.create(restaurantid=rest,foodname=foodname,type=type,category=category,price=price,availability=availability,foodimage=foodimage)
            messages.success(request,f'Food item added successfully')
        return redirect('Hotel-ItemView')

    else:
        return redirect('Hotel-ItemView')
