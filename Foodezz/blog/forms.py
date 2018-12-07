from django import forms
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = (
			'title',
			'body',
			'status',
			'restrict_comment',
		)

class PostEditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = (
			'title',
			'body',
			'status',
			'restrict_comment',
		)

class UserLoginForm(forms.Form):
	username = forms.CharField(label='')
	password = forms.CharField(label='', widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
	content = forms.CharField(
		label="",
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
				'placeholder': 'Text goes Here!!!!',
				'rows':'4', 'cols':'50'
			}
		)
	)
	class Meta:
		model = Comment
		fields = ('content',)