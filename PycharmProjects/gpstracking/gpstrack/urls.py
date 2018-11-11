from django.urls import path,include, re_path
from .import views

urlpatterns = [
    re_path('driver',views.index1,name = "index1"),
    re_path('restaurants' ,views.index2,name = "index2" ),
]