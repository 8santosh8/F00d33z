from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
	if(request.method == 'POST'):
		form = UserRegisterForm(request.POST)
		# Checking the entries in the form is valid or not
		if(form.is_valid()):
			form.save()	
			username=form.cleaned_data.get('username')
			# It is a flash message which tells the user that the account is created
			messages.success(request, f'Your Account Has Been Created! You can now able to Login. {username}!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
	return render(request, 'users/profile.html')
# # message.debug
# # message.info
# # message.success
# # message.warning
# # message.error	