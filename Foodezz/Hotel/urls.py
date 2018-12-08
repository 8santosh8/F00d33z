from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home,name='Hotel-Home'),
    path('ItemView/',views.ItemView,name='Hotel-ItemView'),
    path('Update/',views.Update,name='Hotel-Update'),
    path('AddItem',views.AddItem,name='Hotel-AddItem'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
