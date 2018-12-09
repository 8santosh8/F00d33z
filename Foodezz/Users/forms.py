from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models as UserModels

class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email',)

class User_Details(forms.ModelForm):

    address = forms.CharField(widget=forms.Textarea)
    pincode = forms.DecimalField(widget=forms.TextInput,max_digits=6)
    phone = forms.DecimalField(widget=forms.TextInput,max_digits=10)

    class Meta:
        model = UserModels.User_Profile
        fields = ('phone','address','street','city','pincode',)

class C_Login(forms.Form):
    Username = forms.CharField(max_length=30)
    Password = forms.CharField(widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = UserModels.User_Profile
        fields = ('phone','address','street','city','pincode','image')

class ChangePasswordform(forms.Form):
    Current_password = forms.CharField(widget=forms.PasswordInput,required=True)
    new_Password = forms.CharField(widget=forms.PasswordInput,required=True)
    Re_Password = forms.CharField(widget=forms.PasswordInput,required=True)
