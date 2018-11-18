from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomerLog, RestaurantLog, CustomerCart, RestaurantItems, Orders


# Create your views here.

def restaurantselection(request):
    data1 = RestaurantLog.objects.all()
    data={"restaurantdata":data1}

    rest_id=request.session.get('rest_id',1)
    rest_name=request.session.get('rest_name','swathi')
    #for i in data['restaurantdata']:
    #   print(i.name)
    return render(request, 'payments/restaurant.html',data)


def foodselection(request):

    restaurant = request.POST['restraunt']
    rest=RestaurantLog.objects.filter(name=restaurant)
    for i in rest:
        rest_id=i.id
    data1=RestaurantItems.objects.filter(restaurantid=rest_id)
    data={"food":data1,"rest":restaurant}

    request.session['rest_id']=rest_id
    request.session['rest_name']=restaurant

    #rest update starts here
    if (request.POST['submit'] == 'restaurantupdate'):
        return render(request, 'payments/restaurantupdate.html',data)
    #rest update end here

    #for i in data['food']:
    #   print(i.foodname)
    return render(request, 'payments/foodselection.html',data)

def pay(request):
    buyoradd=request.POST['button']
    if(buyoradd=='add to cart'):
         restname = request.session['my_rest']
        # rest = RestaurantLog.objects.filter(name=restname)
        # for i in rest:
        #     rest_id = i.id
        # rest_ids=str(rest_id)
        # CustomerCart.objects.create()
        # foodname=request.POST['food']
        # CustomerCart.objects.create(customerid='1',restaurantid=rest_ids,foodname=foodname)

    else:
        restname=request.session['rest_name']
        foodname=request.POST['food']

        data={
            'restname':restname,
            'foodname':foodname,
        }

        return render(request,'payments/buynow.html',data)

def restupdate(request):
    rest_id=request.session['rest_id']
    data1=RestaurantItems.objects.filter(restaurantid=rest_id)
    submit=request.POST['submit']
    restaurant=request.session['rest_name']
    data={'rest':restaurant}

    if(submit=='update'):
        for i in data1:
            foodname=i.foodname
            price=request.POST[foodname+'_price']
            availability=request.POST[foodname+'_availability']

            RestaurantItems.objects.filter(restaurantid=rest_id, foodname=foodname).update(price=price,availability=availability)
        return HttpResponse('Updated successfully')

    elif(submit=='newitem'):
        return render(request,'payments/newitem.html',data)


def newitem(request):
    rest_id=request.session['rest_id']
    foodname=request.POST['foodname']
    type=request.POST['type']
    price=request.POST['price']
    availability=request.POST['availability']
    RestaurantItems.objects.create(restaurantid=rest_id,foodname=foodname,type=type,price=price,availability=availability)
    restaurant = request.session['rest_name']
    data = {'rest': restaurant}
    return render(request,'payments/restaurantupdate.html',data)