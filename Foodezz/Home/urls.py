from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home,name='Home-Home'),
    path('Cart/',views.Cart,name='Home-Cart'),

]
