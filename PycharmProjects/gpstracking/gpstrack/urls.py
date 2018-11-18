from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path('driver', views.index1, name="gpstrack.index1"),
    re_path('find', views.getcurrloc, name="find.driver"),
    path('result', views.result, name="gpstrack.results"),
    path('maps', views.map, name="gpstrack.maps")
]

