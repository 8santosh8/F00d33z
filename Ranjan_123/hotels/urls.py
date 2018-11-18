from django.urls import path
from hotels import views

urlpatterns = [
    path('',views.index,name="index" ),

]