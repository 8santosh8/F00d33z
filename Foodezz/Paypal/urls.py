from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('payment-button/',views.payment_button,name = 'payment_button'),  #buy now button of Paypal
    path('paypal/',include('paypal.standard.ipn.urls')),
    # path('paypal-return',views.paypal_return,name = 'paypal_return'),
    # path('paypal-cancel',views.paypal_cancel,name = 'paypal_cancel'),
]
