from django.urls import path

from . import views

app_name = "payments"

urlpatterns=[
    path('search',views.search,name='search'),
    path('pay/<rest>',views.pay,name='pay'),
    path('restupdate',views.restupdate,name='restupdate'),
    path('newitem',views.newitem,name='newitem'),
    path('mycart',views.mycart,name='mycart'),
    path('makecart',views.makecart,name='makecart'),
    path('restorders',views.restorder,name='restorder'),
    path('orderconfirm/<state>/<orderid>',views.orderconfirm,name='orderconfirm'),
    path('locaterestaurants/<location>', views.locaterestaurants, name='locaterestaurants'),
    path('showrestaurant/<restaurant>', views.showrestaurant, name='showrestaurant'),
    path('makeorderconfirm', views.makeorderconfirm, name='makeorderconfirm'),
    path('makeprev', views.makeprev, name='makeprev'),
    path('feedback', views.feedback, name='feedback'),
    path('feedbackthanks', views.feedbackthanks, name='feedbackthanks')
]
