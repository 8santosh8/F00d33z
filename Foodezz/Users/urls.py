from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('Register/',views.Register,name='Users-Register'),
    path('',views.Home,name='Users-Home'),
    path('Login/',views.Login,name='Users-Login'),
    path('Logout/',auth_views.LogoutView.as_view(template_name='Users/Logout.html'),name='Users-Logout'),
    path('Profile/',views.Profile,name='Users-Profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)