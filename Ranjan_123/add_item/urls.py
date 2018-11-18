from django.urls import path
from add_item import views

urlpatterns = [
    path('',views.index,name="index" ),

]