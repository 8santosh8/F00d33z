from payments.models import Orders, CustomerCart, Feedback
from Hotel.models import RestaurantLog, RestaurantItems
from Users.models import User_Profile as CustomerLog
from django.shortcuts import render,redirect
from django.http import HttpResponse
from gpstrack import views as gps
from django.contrib.auth.decorators import login_required
from Paypal import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def search(request):
    var=request.POST['myCountry']
    place=RestaurantLog.objects.values_list('city').distinct()
    rest=RestaurantLog.objects.values_list('name').distinct()
    print(var)
    for i in rest:
        for j in i:
            if (var==j):
                rest_id = RestaurantLog.objects.get(name=var)
                data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
                restaurant = RestaurantLog.objects.all()

                data = {'food': data1, 'rest': var}
                return render(request, 'payments/foodselection.html', data)
    for i in place:
        for j in i:
            if (var==j):
                return locaterestaurants(request, var)


#needed
def makelocations(request):
    location=RestaurantLog.objects.values('city').distinct()
    data={'locations':location}
    return render(request, 'payments/showlocations.html', data)

#needed
def locaterestaurants(request, location):
    #location=request.POST['submit']
    restaurant=RestaurantLog.objects.filter(city=location)
    data={'restaurants':restaurant}
    return render(request, 'payments/locaterestaurants.html', data)

#needed
def showrestaurant(request, restaurant):
    # restaurant=request.POST['submit']
    rest=RestaurantLog.objects.filter(name=restaurant)
    rest_id="1"
    for i in rest:
        rest_id=i.id
    data1=RestaurantItems.objects.filter(restaurantid=rest_id)
    data={'food':data1, 'rest':restaurant}
    return render(request, 'payments/foodselection.html', data)

#needed
@login_required
def pay(request,rest):
    quantity=request.POST['quantity']
    buyoradd=request.POST['button']
    rest_id = RestaurantLog.objects.get(name=rest)

    foodname = request.POST['food']
    # customerid = request.session['customer_id']
    # customer_id = CustomerLog.objects.get(pk=customerid)
    customer_id = request.user

    if(buyoradd=='add to cart'):
        if not CustomerCart.objects.filter(customerid=customer_id, restaurantid=rest_id, foodname=foodname):
            CustomerCart.objects.create(customerid=customer_id, restaurantid=rest_id, foodname=foodname)
        data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
        data = {'food': data1, 'rest': rest}
        return render(request, 'payments/foodselection.html', data)

    else:
        order_id='0'
        if Orders.objects.all():
            orders=Orders.objects.all()
            for i in orders:
                order_id=i.orderid
        orderid=int(order_id)+1
        order_id=str(orderid)
        price=int(RestaurantItems.objects.get(restaurantid=rest_id, foodname=foodname).price)*int(quantity)
        Orders.objects.create(orderid=order_id,customerid=customer_id,restaurantid=rest_id,foodname=foodname,quantity=quantity,price=price,status='SentToRestaurant')

        data1 = RestaurantItems.objects.filter(restaurantid=rest_id)
        restaurant=rest_id.name
        data = {'food': data1, 'rest': restaurant}
        return views.payment_button(request, foodname, quantity, price, orderid)

#needed
@login_required
def mycart(request):
    state=request.POST['button']
    food = request.POST['food_id']


    if(state=='buynow'):

        q=food+'_quantity'
        print(q)
        quantity = request.POST[str(q)]
        food=CustomerCart.objects.filter(pk=food)
        for i in food:
            foodname=i.foodname
            rest_id=i.restaurantid
        customer_id = request.user

        order_id = '0'
        if Orders.objects.all():
            orders = Orders.objects.all()
            for i in orders:
                order_id = i.orderid
        orderid = int(order_id) + 1
        order_id = str(orderid)

        print(foodname, rest_id, quantity)
        price = int(RestaurantItems.objects.get(restaurantid=rest_id, foodname=foodname).price) * int(quantity)
        Orders.objects.create(orderid=order_id, customerid=customer_id, restaurantid=rest_id, foodname=foodname,
                              quantity=quantity, price=price, status='SentToRestaurant')

        return views.payment_button(request, foodname, quantity, price, orderid)

    elif(state=='remove from cart'):
        CustomerCart.objects.filter(pk=food).delete()

    return makecart(request)

#needed
@login_required
def makecart(request):
    if request.user.is_authenticated:
        later = CustomerCart.objects.filter(customerid=request.user.id)
        restdata = RestaurantLog.objects.all()
        food=RestaurantItems.objects.all()
        data = {'later': later, 'rest': restdata, 'food':food}
        return render(request, 'payments/mycart.html', data)


#needed
@login_required
def makeorderconfirm(request):
    # cust_id=CustomerLog.objects.get(pk=request.session['customer_id'])
    if request.user.is_authenticated:
        cust_id=request.user.id
        order=Orders.objects.filter(customerid=cust_id,status__in=['SentToRestaurant','OutForDelivery'])
        restdata=RestaurantLog.objects.all()
        data = {'orders':order, 'rest':restdata}
        return render(request, 'payments/orderconfirmation.html', data)

#needed
@login_required
def orderconfirm(request,state,orderid):
    if state=='track':
        driver=Orders.objects.get(orderid=orderid)
        return gps.map(request, driver.deliveryid)
    else:
        Orders.objects.filter(orderid=orderid).update(status='success')
        #feedback
        subject='Feedback'
        message=render_to_string('payments/email.html')
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['santosh.p17@iiits.in']
        send_mail(subject, message, email_from, recipient_list)

        return makeorderconfirm(request)

def feedback(request):
    return render(request, 'payments/feedback.html')

def feedbackthanks(request):
    rate=request.POST['rate']
    suggestion=request.POST['suggestion']
    print(rate,suggestion)
    Feedback.objects.create(rate=rate, suggestion=suggestion)
    return render(request, 'payments/feedbackthanks.html')

@login_required
def makeprev(request):
    cust_id=request.user.id
    order=Orders.objects.filter(customerid=cust_id, status='success')
    restdata = RestaurantLog.objects.all()
    data={'order':order, 'rest':restdata}
    return render(request, 'payments/previousbookings.html', data)


####################################################################################################################
#Restaurant


#needed
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

#needed
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

#needed
def makerestupdate(request):
    data1 = RestaurantItems.objects.filter(restaurantid=request.session['rest_id'])
    order = Orders.objects.filter(restaurantid=request.session['rest_id'], status='SentToRestaurant')
    inprogress = Orders.objects.filter(restaurantid=request.session['rest_id'], status='OutForDelivery')
    data = {"food": data1, "rest": request.session['rest_name'], "orders": order, "inpro":inprogress}
    return render(request, 'payments/restaurantupdate.html', data)

#needed
def restorder(request):
    Orders.objects.filter(orderid=request.POST['orderid']).update(deliveryid=request.POST['deliveryid'], status='OutForDelivery')
    return makerestupdate(request)
