from django.urls import path

from . import views

urlpatterns=[
    path('',views.restaurantselection,name='restaurantselection'),
    path('foodselection',views.foodselection,name='foodselection'),
]