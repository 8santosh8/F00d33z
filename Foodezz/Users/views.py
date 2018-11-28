from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Users.forms import C_Login
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
            return redirect('Users-Home')
    else:
        User_Form1 = forms.UserForm()
        User_Details1 = forms.User_Details()
    return render(request, 'Users/Register.html', {'User_Form1': User_Form1, 'User_Details1':User_Details1})

def Home(request):
    return render(request,'Users/Home.html',)

def Login(request):
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
    return render(request,'Users/Profile.html',{})