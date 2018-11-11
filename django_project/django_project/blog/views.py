from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse

# posts = [
# 	{
# 		'author': 'AmanG',
# 		'title': 'Blog Post 1',
# 		'content': 'First post content',
# 		'date_posted': 'August 27, 2018'
# 	},	
# 	{
# 		'author': 'Subu K',
# 		'title': 'Blog Post 2',
# 		'content': 'Second post content',
# 		'date_posted': 'August 28, 2018'
# 	}
# ]
@login_required
def home(request):
	posts = Post.objects.all()
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)
	# return HttpResponse('<h1>Blog Home</h1>')
def about(request):
	return render(request, 'blog/about.html', {'title':'About'})
	# return HttpResponse('<h1>Blog Home</h1>')