from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomerLog, RestaurantLog, CustomerCart, RestaurantItems, Orders
from gpstrack import views as gps


# Create your views here.

def restaurantselection(request):
    data1 = RestaurantLog.objects.all()
    data={"restaurantdata":data1}
    customer = CustomerLog.objects.filter(name='santosh')
    for i in customer:
        customer_id=i.id
    # customer=request.session.get('customer_id',customer_id)
    request.session['customer_id']=customer_id
    rest_id=request.session.get('rest_id',1)
    rest_name=request.session.get('rest_name','swathi')
    return render(request, 'payments/restaurant.html',data)


def foodselection(request):

    restaurant = request.POST['restaurant']
    rest=RestaurantLog.objects.filter(name=restaurant)
    for i in rest:
        rest_id=i.id
    data1=RestaurantItems.objects.filter(restaurantid=rest_id)
    data={"food":data1,"rest":restaurant}

    request.session['rest_id']=rest_id
    request.session['rest_name']=restaurant

    if (request.POST['submit'] == 'restaurantupdate'):
        return makerestupdate(request)

    elif(request.POST['submit']=='my cart'):
        return makecart(request)

    elif(request.POST['submit']=='makeorderconfirmation'):
        return makeorderconfirm(request)

    elif (request.POST['submit'] == 'showalllocations'):
        return makelocations(request)
    else:
        return render(request, 'payments/foodselection.html', data)

def makelocations(request):
    location=RestaurantLog.objects.values('city').distinct()
    data={'locations':location}
    return render(request, 'payments/showlocations.html', data)

def locaterestaurants(request, location):
    #location=request.POST['submit']
    restaurant=RestaurantLog.objects.filter(city=location)
    data={'restaurants':restaurant}
    return render(request, 'payments/locaterestaurants.html', data)

def showrestaurant(request, restaurant):
    # restaurant=request.POST['submit']
    rest=RestaurantLog.objects.filter(name=restaurant)
    for i in rest:
        rest_id=i.id
    request.session['rest_name']=restaurant
    request.session['rest_id']=rest_id
    data1=RestaurantItems.objects.filter(restaurantid=rest_id)
    data={'food':data1, 'rest':restaurant}
    return render(request, 'payments/foodselection.html', data)


def pay(request):
    quantity=request.POST['quantity']
    buyoradd=request.POST['button']
    restid = request.session['rest_id']
    rest_id = RestaurantLog.objects.get(pk=restid)
    foodname = request.POST['food']
    # customerid = request.session['customer_id']
    # customer_id = CustomerLog.objects.get(pk=customerid)
    customer_id = request.user

    if(buyoradd=='add to cart'):

        if (buyoradd=='add to cart'):
            if not CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname):
                CustomerCart.objects.create(customerid=customer_id, restaurantid=rest_id, foodname=foodname)

    else:
        order_id='0'
        if Orders.objects.all():
            orders=Orders.objects.all()
            for i in orders:
                order_id=i.orderid
        orderid=int(order_id)+1
        order_id=str(orderid)
        price=quantity*int(RestaurantItems.objects.get(restaurantid=rest_id, foodname=foodname).price)
        Orders.objects.create(orderid=order_id,customerid=customer_id,restaurantid=rest_id,foodname=foodname,quantity=quantity,price=price,status='SentToRestaurant')

    data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
    restaurant = request.session['rest_name']
    data = {'food': data1, 'rest': restaurant}
    return render(request, 'payments/foodselection.html', data)


def mycart(request):
    button=request.POST['button']
    food = request.POST['food_id']
    
    if(button=='buynow'):
        return HttpResponse('yoyo')

    elif(button=='remove from cart'):
        CustomerCart.objects.filter(pk=food).delete()

    return makecart(request)

#used
def makecart(request):
    if request.user.is_authenticated:
        later = CustomerCart.objects.filter(customerid=request.user.id)
        restdata = RestaurantLog.objects.all()
        data = {'later': later, 'rest': restdata}
        return render(request, 'payments/mycart.html', data)


def makebuynow(request):
    cust_id=CustomerLog.objects.get(pk=request.session['customer_id'])
    fooddata=CustomerCart.objects.filter(customerid=cust_id)
    restdata=RestaurantLog.objects.all()
    data={'food':fooddata,'rest':restdata}
    return render(request, 'payments/buynow.html', data)

#used
def makeorderconfirm(request):
    # cust_id=CustomerLog.objects.get(pk=request.session['customer_id'])
    if request.user.is_authenticated:
        cust_id=request.user.id
        order=Orders.objects.filter(customerid=cust_id,status__in=['SentToRestaurant','OutForDelivery'])
        restdata=RestaurantLog.objects.all()
        data = {'orders':order, 'rest':restdata}
        return render(request, 'payments/orderconfirmation.html', data)

#used
def orderconfirm(request,state,orderid):
    if state=='track':
        driver=Orders.objects.get(orderid=orderid)
        return gps.map(request, driver.deliveryid)



####################################################################################################################
#Restaurant


def restupdate(request):
    submit = request.POST['submit']

    if(submit=='Update'):
        rest_id = request.session['rest_id']
        data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
        for i in data1:
            foodname=i.foodname
            price=request.POST[foodname+'_price']
            availability=request.POST[foodname+'_availability']
            RestaurantItems.objects.filter(restaurantid=rest_id, foodname=foodname).update(price=price,availability=availability)
        return makerestupdate(request)

    elif(submit=='Add New Item'):
        restaurant = request.session['rest_name']
        data = {'rest': restaurant}
        return render(request,'payments/newitem.html',data)

    else:
        foodname=request.POST['foodname']
        rest_id = request.session['rest_id']
        RestaurantItems.objects.filter(restaurantid=rest_id, foodname=foodname).delete()
        return makerestupdate(request)


def newitem(request):
    restid=request.session['rest_id']
    rest_id=RestaurantLog.objects.get(pk=restid)
    foodname=request.POST['foodname']
    type=request.POST['type']
    category=request.POST['category']
    price=request.POST['price']
    availability=request.POST['availability']
    foodimage=request.FILES['foodimage']
    if RestaurantItems.objects.filter(foodname=foodname):
        return HttpResponse('Same foodname exists try creating with other food name.')
    else:
        RestaurantItems.objects.create(restaurantid=rest_id,foodname=foodname,type=type,category=category,price=price,availability=availability,foodimage=foodimage)
        data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
        restaurant = request.session['rest_name']
        data = {'food': data1, 'rest': restaurant}
        return render(request, 'payments/restaurantupdate.html', data)


def makerestupdate(request):
    data1 = RestaurantItems.objects.filter(restaurantid=request.session['rest_id'])
    order = Orders.objects.filter(restaurantid=request.session['rest_id'], status='SentToRestaurant')
    inprogress = Orders.objects.filter(restaurantid=request.session['rest_id'], status='OutForDelivery')
    data = {"food": data1, "rest": request.session['rest_name'], "orders": order, "inpro":inprogress}
    return render(request, 'payments/restaurantupdate.html', data)


def restorder(request):
    Orders.objects.filter(orderid=request.POST['orderid']).update(deliveryid=request.POST['deliveryid'], status='OutForDelivery')
    return makerestupdate(request)