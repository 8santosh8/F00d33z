from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from Users.forms import C_Login
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from Foodezz.settings import EMAIL_HOST_USER
from . import decorators

def Register(request):
    if request.user.is_authenticated:
        messages.info(request, f'You are already logged in!, Log out to login from different account')
        return redirect('Users-Home')
    if(request.method == 'POST'):
        User_Form1 = forms.UserForm(request.POST)
        User_Details1 = forms.User_Details(request.POST,request.FILES)
        if User_Form1.is_valid() and User_Details1.is_valid():
            # print(User_Details1.cleaned_data.get('image'))
            if User.objects.filter(email = User_Form1.cleaned_data.get('email')).exists():
                messages.error(request, f'Email already exists go to login page to login')
                return render(request, 'Users/Register.html',
                              {'User_Form1': User_Form1, 'User_Details1': User_Details1})

            if len(str(User_Details1.cleaned_data.get('phone'))) is not 10:             ## For phone number to have 10 digits
                messages.error(request, f'Phone number should be of ten digits')
                return render(request, 'Users/Register.html', {'User_Form1': User_Form1, 'User_Details1':User_Details1})

            if len(str(User_Details1.cleaned_data.get('pincode'))) is not 6:            ## For pincode to have 6 digits
                messages.error(request,f'Enter valid pincode details')
                return render(request, 'Users/Register.html', {'User_Form1': User_Form1, 'User_Details1':User_Details1})

            username = User_Form1.cleaned_data.get('username')
            newuser_basic = User_Form1.save(commit=False)
            newuser_basic.is_active = False
            newuser_basic.save()
            newuser = User_Details1.save(commit=False)
            newuser.User = newuser_basic
            newuser.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Food3zz account.'
            message = render_to_string('Users/acc_active_email.html', {
                'user': newuser_basic,
                'domain': current_site.domain,
                # 'uid': urlsafe_base64_encode(force_bytes(newuser_basic.pk)),
                'uid': newuser_basic.pk,
                'token': account_activation_token.make_token(newuser_basic),
            })
            to_email = User_Form1.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, f'confirm your mail to complete registration for {username}!')
            return redirect('Users-Login')
    else:
        User_Form1 = forms.UserForm()
        User_Details1 = forms.User_Details()
    return render(request, 'Users/Register.html', {'User_Form1': User_Form1, 'User_Details1':User_Details1})


def activateAccout(request, uidb64, token):
    try:
        print(uidb64 + "   " + token)
        # uid = force_text(urlsafe_base64_decode(uidb64))
        print(int(uidb64))
        uid = uidb64
        user = User.objects.get(pk=int(uid))

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, f'Account created successfully!')
            return redirect('Users-Home')
        else:
            return HttpResponse('Didnt match the token')
    else:
        return HttpResponse('Activation link is invalid!')


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

        if user and user.user_profile.rest == False:
            if user.is_active:
                login(request,user)
                return redirect('Users-Home')
            else:
                messages.error(request,f'Account not in active state')
                return redirect('User-Login')
        else:
            messages.error(request, f'Invalid login details')
            Log_form = C_Login(request.POST)
    else:
        Log_form = C_Login()
    return render(request,'Users/Login.html',{'Login_form':Log_form})

@decorators.Details_Required
def Profile(request,username):
    if not hasattr(request.user, 'user_profile'):
        return redirect('Users-AddDetails')
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, files=request.FILES, instance=request.user.user_profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('Users-Profile',request.user.username)

    else:
        u_form = forms.UserUpdateForm(instance= request.user)
        p_form = forms.ProfileUpdateForm(instance= request.user.user_profile)

    return render(request,'Users/Profile.html',{'u_form':u_form,'p_form':p_form,})


def RestLogin(request):
    if request.user.is_authenticated:
        messages.info(request, f'You are already logged in!, Log out to login from different account')
        return redirect('Users-Home')
    if request.method == "POST":
        name = request.POST.get('Username')
        pword = request.POST.get('Password')

        user = authenticate(username=name, password=pword)
        if user and user.user_profile.rest == True:
            if user.is_active:
                login(request, user)
                return redirect('Users-Home')
            else:
                messages.error(request, f'Account not in active state')
                return redirect('Users-Login')
        else:
            messages.error(request, f'Invalid login details')
            Rest_Login_Form = C_Login(request.POST)
    else:
        Rest_Login_Form = C_Login()
    return render(request,'Users/Rest-Login.html',{'Login_form':Rest_Login_Form})

@decorators.Details_Required
def ChangePassword(request):
    if request.method == 'POST':
        ChangePassForm = forms.ChangePasswordform(request.POST)
                                                                            # validate the password given
        pword = request.POST.get('Current_password')
        # print('got password')
        uname = request.user.username
        # print('got username')
        user = authenticate(username=uname,password=pword)

        if user == request.user:
                                                                                            # Check same password in both fields
            new_Password = request.POST.get('new_Password')
            # print(new_Password)
            new_Password1 = request.POST.get('Re_Password')
            # print(new_Password1)

            if new_Password == new_Password1:

                if len(new_Password) <= 4:                                              # Check for password meets the minimum security
                    messages.error(request, f'Password should more then 4 characters')
                    return redirect('Users-ChangePassword')

                else:
                    user.set_password(new_Password)                                                # Change the password for the user and logout.
                    user.save()

                                                                                                    # Mail the user about the change in password
                    mail_subject = "Hi, "+ user.username + " alert for Food3zz account"
                    message = "Your Food3zz account password has been changed. /nIf you didn't change the password you can always go to our home page and reset your password."
                    mail_address = user.email
                    # print(user.email)
                    send_mail(mail_subject, message, 'EMAIL_HOST_USER',[mail_address], fail_silently=True)

                    messages.success(request, f"Password successfully changed, now login to your account")
                    return redirect('Users-Login')

            else:
                messages.error(request, f"Passwords didn't match")

        else:
            messages.error(request,f'User can not be found')

    else:
        ChangePassForm = forms.ChangePasswordform()
    return render(request,'Users/ChangePassword.html',{'ChangePassForm':ChangePassForm})

@login_required
def AddDetails(request):
    if not hasattr(request.user, 'user_profile'):
        if request.method == 'POST':
            p_form = forms.ProfileUpdateForm(request.POST,request.FILES)
            if p_form.is_valid():
                newUser = p_form.save(commit=False)
                newUser.User = request.user
                newUser.save()
                messages.success(request, f"User details added successfully")
                return redirect('Users-Home')
            else:
                messages.error(request,f"User details invalid")
        else:
            p_form = forms.ProfileUpdateForm()

        return render(request,'Users/AddDetails.html',{'p_form':p_form,})
    else:
        return redirect('Users-Profile', request.user.username)
