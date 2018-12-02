from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomerLog, RestaurantLog, CustomerCart, RestaurantItems, Orders


# Create your views here.

def restaurantselection(request):
    data1 = RestaurantLog.objects.all()
    data={"restaurantdata":data1}
    customer = CustomerLog.objects.filter(name='santosh')
    for i in customer:
        customer_id=i.id
    customer=request.session.get('customer_id',customer_id)
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
        return render(request, 'payments/restaurantupdate.html',data)

    elif(request.POST['submit']=='my cart'):
        return makecart(request)

    else:
        return render(request, 'payments/foodselection.html', data)

def pay(request):
    buyoradd=request.POST['button']
    if(buyoradd=='add to cart' or buyoradd=='add to buynow'):
        restid = request.session['rest_id']
        rest_id=RestaurantLog.objects.get(pk=restid)
        foodname=request.POST['food']
        customerid=request.session['customer_id']
        customer_id=CustomerLog.objects.get(pk=customerid)

        if (buyoradd=='add to cart'):
            if not CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname):
                CustomerCart.objects.create(customerid=customer_id, restaurantid=rest_id, foodname=foodname,
                                            status='later')
            elif not CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname, status='later'):
                CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname).update(
                    status='both')
        else:
            if not CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname):
                CustomerCart.objects.create(customerid=customer_id, restaurantid=rest_id, foodname=foodname,
                                            status='buynow')
            elif not CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname, status='buynow'):
                CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname).update(
                    status='both')

        data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
        restaurant = request.session['rest_name']
        data = {'food': data1, 'rest': restaurant}
        return render(request,'payments/foodselection.html', data)

    else:
        return makebuynow(request)



def mycart(request):
    button=request.POST['button']
    food = request.POST['food_id']
    
    if(button=='buynow'):
        return HttpResponse('yoyo')

    elif(button=='remove from buynow' or button=='remove from cart'):

        if not CustomerCart.objects.filter(pk=food, status='both'):
            CustomerCart.objects.filter(pk=food).delete()
        else:
            if(button=='remove from buynow'):
                CustomerCart.objects.filter(pk=food).update(status='later')
            else:
                CustomerCart.objects.filter(pk=food).update(status='buynow')

    elif (button == 'add to buynow' or button == 'add to cart'):
        CustomerCart.objects.filter(pk=food).update(status='both')

    return makecart(request)


def makecart(request):
    buynow = CustomerCart.objects.filter(customerid=request.session['customer_id'], status__in=['buynow', 'both'])
    later = CustomerCart.objects.filter(customerid=request.session['customer_id'], status__in=['later', 'both'])
    restdata = RestaurantLog.objects.all()
    data = {'buynow': buynow, 'later': later, 'rest': restdata}
    return render(request, 'payments/mycart.html', data)


def makebuynow(request):
    cust_id=CustomerLog.objects.get(pk=request.session['customer_id'])
    fooddata=CustomerCart.objects.filter(customerid=cust_id,status__in=['both','buynow'])
    restdata=RestaurantLog.objects.all()
    data={'food':fooddata,'rest':restdata}
    return render(request, 'payments/buynow.html', data)


####################################################################################################################
#Restaurant

def restupdate(request):
    submit = request.POST['submit']

    if(submit=='update'):
        rest_id = request.session['rest_id']
        data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
        for i in data1:
            foodname=i.foodname
            price=request.POST[foodname+'_price']
            availability=request.POST[foodname+'_availability']
            RestaurantItems.objects.filter(restaurantid=rest_id, foodname=foodname).update(price=price,availability=availability)
        return makerestupdate(request)

    elif(submit=='newitem'):
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
    price=request.POST['price']
    availability=request.POST['availability']
    if RestaurantItems.objects.filter(foodname=foodname):
        return HttpResponse('Same foodname exists try creating with other food name.')
    else:
        RestaurantItems.objects.create(restaurantid=rest_id,foodname=foodname,type=type,price=price,availability=availability)
        data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
        restaurant = request.session['rest_name']
        data = {'food': data1, 'rest': restaurant}
        return render(request, 'payments/restaurantupdate.html', data)


def makerestupdate(request):
    rest_id=request.session['rest_id']
    data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
    restaurant = request.session['rest_name']
    data = {'food': data1, 'rest': restaurant}
    return render(request, 'payments/restaurantupdate.html', data)
