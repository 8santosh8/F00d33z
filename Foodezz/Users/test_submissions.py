from django.test import TestCase, Client
from django.contrib.auth.models import User
from Users import models
from . import forms

class RegisterSubmitTest(TestCase):
    def setUp(self):
        self.request_url = '/Register/'

    def test_submit(self):
        self.client = Client()
        response = self.client.post(self.request_url,
                                {'username':'Dummy',
                                'first_name':'Dumm',
                                'last_name':'dull',
                                'password1':'hello1234567',
                                'password2':'hello1234567',
                                'email':'hello@cool.com',
                                'phone':7894561230,
                                'address':'asldfkir',
                                'street':'sfdc',
                                'city':'klsjfd',
                                'pincode':789456,})

        self.assertRedirects(response,expected_url='/Login/')

class CustLoginTest(TestCase):
    def setUp(self):
        self.RegisteredUser = User.objects.create(username='Test',email='test@testing.com',password='HelloWorld')
        user_details = models.User_Profile.objects.create(User=self.RegisteredUser,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.RegisteredUser.user_profile = user_details
        self.client = None
        self.request_url = '/Login/'

    def test_submit(self):
        self.client = Client()
        response = self.client.post(self.request_url,
                                    {'Username':'Test',
                                    'Password':'HelloWorld'})

        self.assertEqual(response.status_code,200)

class ProfileUpdateTest(TestCase):
    def setUp(self):
        self.RegisteredUser = User.objects.create(username='Test',email='test@testing.com',password='HelloWorld')
        user_details = models.User_Profile.objects.create(User=self.RegisteredUser,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.RegisteredUser.user_profile = user_details
        self.client = None
        self.request_url = '/Profile/'

    def test_unautherizedSubmit(self):
        self.client = Client()
        response = self.client.post(self.request_url,
                                    {'username':'newName',
                                    'first_name':'newfirst',
                                    'last_name':'newLast',
                                    'email':'new@email.com',
                                    'phone':9876543210,
                                    'address':'newaddress',
                                    'street':'newstreet',
                                    'city':'newcity',
                                    'pincode':'456789',})

        self.assertEqual(response.status_code,404)

    def test_autherizedSubmit(self):
        self.client = Client()
        self.client.force_login(self.RegisteredUser)
        response = self.client.post(self.request_url+self.RegisteredUser.username,
                                    {'username':'newName',
                                    'first_name':'newfirst',
                                    'last_name':'newLast',
                                    'email':'new@email.com',
                                    'phone':9876543210,
                                    'address':'newaddress',
                                    'street':'newstreet',
                                    'city':'newcity',
                                    'pincode':'456789',})
        # self.assertEqual(response.status_code,302)
        self.assertRedirects(response,expected_url='/Profile/newName')

class ChangePasswordTest(TestCase):
    def setUp(self):
        self.RegisteredUser = User.objects.create(username='Test',email='test@testing.com',password='HelloWorld')
        user_details = models.User_Profile.objects.create(User=self.RegisteredUser,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.RegisteredUser.user_profile = user_details
        self.client = None
        self.request_url = '/ChangePassword/'

    def test_unautherizedSubmit(self):
        self.client = Client()
        response = self.client.post(self.request_url,
                                    {'Current_password':'HelloWorld',
                                    'new_Password':'newPassword',
                                    'Re_Password':'newPassword'})

        # self.assertEqual(response.status_code,404)
        self.assertRedirects(response,expected_url='/Login/')

    def test_autherizedSubmit(self):
        self.client = Client()
        self.client.force_login(self.RegisteredUser)
        response = self.client.post(self.request_url,
                                    {'Current_password':'HelloWorld',
                                    'new_Password':'newPassword',
                                    'Re_Password':'newPassword'})

        # self.assertRedirects(response,expected_url='/Login/')
        self.assertEqual(response.status_code,200)
