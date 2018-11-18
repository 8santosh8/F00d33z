from django.shortcuts import render, redirect

# This will be the by default inbuilt views 
from django.views.generic import (
	ListView,
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
# from django.http import HttpResponse

# This is home function
@login_required
def home(request):
	posts = Post.objects.all()
	context = {
		'posts': Post.objects.all()
	}
	print(posts)
	return render(request, 'blog/home.html', {'posts':posts})
	# return HttpResponse('<h1>Blog Home</h1>')

#  this is home list view

# class PostListView(ListView):
# 	model = Post
# 	template_name = 'blog/home.html' #app/<model>_<viewtype>.html
# 	context_object_name = 'posts'
# 	query = request.GET.get('q')
# 	posts = Post.objects.all().order_by('-date_posted')
# 	if(query):
# 		if(User.objects.filter(username=query)):
# 			yo_id=User.objects.get(username=query)
# 			posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author=yo_id)).order_by('-date_posted')
# 		else:
# 			posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-date_posted')
# 	ordering = ['-date_posted']

@login_required
def PostListViews(request):
	query = request.GET.get('q')
	posts = Post.objects.all().order_by('-date_posted')
	if(query):
		if(User.objects.filter(username=query)):
			yo_id=User.objects.get(username=query)
			posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author=yo_id)).order_by('-date_posted')
		else:
			posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-date_posted')
	return render(request,'blog/home.html',{"posts":posts})

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user	
		return super().form_valid(form)

#UserPassesTestMixin will check if the user if able to update only his 
#post if not then a login page will be displayed
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user	
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		# checking if the author is trying to update his blog post
		if(self.request.user == post.author):
			return True
		else:
			return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	#author should be logged in 
	# author should be able to delete his post only not others
	# Adding success urls so that it will redirect and delete the post
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		# checking if the author is trying to update his blog post
		if(self.request.user == post.author):
			return True
		else:
			return False

# @login_required
# def PostListView(request):
# 	query = request.GET.get('q')
# 	posts = Post.objects.all().order_by('-date_posted')
# 	if(query):
# 		if(User.objects.filter(username=query)):
# 			yo_id=User.objects.get(username=query)
# 			posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author=yo_id)).order_by('-date_posted')
# 		else:
# 			posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-date_posted')
# 	return render(request,'blog/home.html',{"posts":posts})

# class PostDetailView(DetailView):
# 	model = Post
# @login_required
# def create_post(request):

# 	if request.method == "POST":
# 		form = PostCreateForm(request.POST)

# 		if form.is_valid():
# 			post = form.save(commit=False)
# 			post.author = request.user
# 			post.save()
# 			return redirect('blog-home')
	
# 	else:
# 		form = PostCreateForm()

# 	return render(request, "blog/post_form.html", {"form":form})
# # @login_required
# # def update_post(request,pk):

# # 	if request.method == "POST":
# # 		form = PostCreateForm(request.POST)

# # 		if form.is_valid():
# # 			post = form.save(commit=False)
# # 			post.author = request.user
# # 			post.save()
# # 			return redirect('blog-home')
	
# # 	else:
# # 		form = PostCreateForm()

# # 	return render(request, "blog/post_form.html", {"form":form})				

@login_required
def about(request):
	return render(request, 'blog/about.html', {'title':'About'})
	# return HttpResponse('<h1>Blog Home</h1>')



