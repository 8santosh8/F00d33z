from django.urls import path

from . import views

app_name = "payments"

urlpatterns=[
    path('',views.restaurantselection,name='restaurantselection'),
    path('foodselection',views.foodselection,name='foodselection'),
    path('pay',views.pay,name='pay'),
    path('restupdate',views.restupdate,name='restupdate'),
    path('newitem',views.newitem,name='newitem'),
    path('mycart',views.mycart,name='mycart'),
    path('makecart',views.makecart,name='makecart'),
    path('restorders',views.restorder,name='restorder'),
    path('orderconfirm/<state>/<orderid>',views.orderconfirm,name='orderconfirm'),
    path('locaterestaurants/<location>', views.locaterestaurants, name='locaterestaurants'),
    path('showrestaurant/<restaurant>', views.showrestaurant, name='showrestaurant'),
    path('makeorderconfirm', views.makeorderconfirm, name='makeorderconfirm'),
]
