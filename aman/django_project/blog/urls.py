from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required, permission_required
from .views import (
	PostListViews,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)
# app_name = 'blog'
urlpatterns = [
    path('', PostListViews, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),    
    
    # As the user can go to the individual post
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
	
	# It will go to the individual post and from there we can update the post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

