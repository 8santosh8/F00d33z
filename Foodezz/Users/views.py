from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Users.forms import C_Login
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Register(request):
    if(request.method == 'POST'):
        User_Form1 = forms.UserForm(request.POST)
        User_Details1 = forms.User_Details(request.POST)
        if User_Form1.is_valid() and User_Details1.is_valid():
            username = User_Form1.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            newuser_basic = User_Form1.save()
            newuser = User_Details1.save(commit=False)
            newuser.User = newuser_basic
            newuser.save()
            return redirect('Users-Login')
    else:
        User_Form1 = forms.UserForm()
        User_Details1 = forms.User_Details()
    return render(request, 'Users/Register.html', {'User_Form1': User_Form1, 'User_Details1':User_Details1})

def Home(request):
    return render(request,'Users/Home.html',)

def Login(request):
    if request.user.is_authenticated:
        messages.info(request,f'You are already logged in!')
        return redirect('Users-Home')
    if request.method == 'POST':

        name = request.POST.get('Username')
        pword = request.POST.get('Password')

        user = authenticate(username=name,password=pword)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('Users-Home')
            else:
                messages.error(request,f'Account not in active state')
                return redirect('User-Login')
        else:
            messages.error(request, f'Invalid login details')
            return redirect('Users-Login')
    Log_form = C_Login()
    return render(request,'Users/Login.html',{'Login_form':Log_form})

@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('Users-Profile')
    else:
        u_form = forms.UserUpdateForm(instance= request.user)
        p_form = forms.ProfileUpdateForm(instance= request.user.user_profile)

    return render(request,'Users/Profile.html',{'u_form':u_form,'p_form':p_form})
