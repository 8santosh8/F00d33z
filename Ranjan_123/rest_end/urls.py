from django.urls import path
from rest_end import views

urlpatterns = [
    path('',views.index,name="index" ),

]