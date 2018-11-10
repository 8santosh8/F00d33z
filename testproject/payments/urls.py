from django.urls import path

from . import views

urlpatterns=[
    path('',views.restaurantselection,name='restaurantselection'),
    path('foodselection',views.foodselection,name='foodselection'),
    path('pay',views.pay,name='pay'),
    path('restupdate',views.restupdate,name='restupdate'),
    path('newitem',views.newitem,name='newitem'),
]