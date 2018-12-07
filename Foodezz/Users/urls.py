from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    ## Path for registrations of users
    path('Register/',views.Register,name='Users-Register'),
    path('',views.Home,name='Users-Home'),

    ## Paths for Email verification
    path('activate/<uidb64>/<token>/',
        views.activateAccout, name='Users-Activate'),

    ### Paths for the password reset
    path('Password-Reset/', auth_views.PasswordResetView.as_view(template_name='Users/Password-Reset.html'),
         name='password_reset'),
    path('Password-Reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Users/Password-Reset-Done.html'),
         name='password_reset_done'),
    path('Password-Reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Users/Password-Reset-Confirm.html'),
         name='password_reset_confirm'),
    path('Password-Reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Users/Password-Reset-Complete.html'),
         name='password_reset_complete'),

    ## Path for editing profile
    path('Profile/<username>',views.Profile,name='Users-Profile'),
    path('ChangePassword/',views.ChangePassword,name='Users-ChangePassword'),

    ## Path for Login and Logout
    path('Login/', views.Login, name='Users-Login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='Users/Logout.html'), name='Users-Logout'),

    # Path for Resturent login
    path('Rest_Login/',views.RestLogin,name='Rest-Login'),

    ## Path for Login through google api
    path('auth/',include('social_django.urls',namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
