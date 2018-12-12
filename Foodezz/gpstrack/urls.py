from django.urls import path, re_path
from . import views

# app_name = "gpstrack"

urlpatterns = [
    re_path('driver/', views.index1, name="gpstrack.index1"),
    #re_path('find', views.getcurrloc, name="find.driver"),
    path('result/', views.result, name="gpstrack.result"),
    path('maps/<driver>', views.map, name="gpstrack.maps"),
    #path('getpos',views.coord,name="gpstrack.getcoods")
]
