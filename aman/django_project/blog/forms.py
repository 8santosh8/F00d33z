from django.forms import ModelForm
from .models import Post 

class PostCreateForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']