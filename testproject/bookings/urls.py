from django.urls import path

from . import views

urlpatterns=[
    path('',views.loginorsignup,name='loginorsignup'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('signupsubmit',views.signupsubmit,name='signupsubmit'),
    path('loginsubmit',views.loginsubmit,name='loginsubmit'),
]