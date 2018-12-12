from django.test import TestCase, Client
from django.contrib.auth.models import User
from Users import models

class RegisterUrlsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.client = None
        self.request_url = '/Register/'

    def test_unautherizedEntry(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)

    def test_autherizedEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url)

        # self.assertEqual(response.status_code,302)
        self.assertRedirects(response,expected_url='/')

    def test_autherizedEntryRandom(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url+'randomurl')
        self.assertEqual(response.status_code,404)

    def test_unautherizedRandomUrl(self):
        self.client = Client()
        response = self.client.get(self.request_url+'randomurlqwe')
        self.assertEqual(response.status_code,404)

class LoginURLTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.client = None
        self.request_url = '/Login/'

    def test_unautherizedEntry(self):
        self.client = Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code,200)

    def test_autherizedEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url)
        self.assertRedirects(response,expected_url='/')

    def test_autherizedEntryRandom(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url+'randomurl')
        self.assertEqual(response.status_code,404)

    def test_unautherizedRandomUrl(self):
        self.client = Client()
        response = self.client.get(self.request_url+'randomurlqwe')
        self.assertEqual(response.status_code,404)

class AdddetatilsUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.user2 = User.objects.create(username='tester2',email='tester@2.com',password='testthisuseralso')
        self.client = None
        self.request_url = '/AddDetails/'

    def test_autherizedCompleteUserEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url)

        self.assertRedirects(response,expected_url='/Profile/testuser')

    def test_autherizedIncompleteUserEntry(self):
        self.client = Client()
        self.client.force_login(self.user2)
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)

    def test_unautherizedEntry(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertRedirects(response,expected_url='/Login/?next=/AddDetails/')

    def test_autherizedCompleteUserEntryRandom(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url+'randomurl')

        self.assertEqual(response.status_code,404)
        # self.assertRedirects(response,expected_url='/Profile/')

    def test_autherizedIncompleteUserEntryRandom(self):
        self.client = Client()
        self.client.force_login(self.user2)
        response = self.client.get(self.request_url+'randomurl')

        self.assertEqual(response.status_code,404)
        # self.assertEqual(response.status_code,200)

    def test_unautherizedEntryRandom(self):
        self.client = Client()
        response = self.client.get(self.request_url+'randomurl')

        # self.assertRedirects(response,expected_url='/Login')
        self.assertEqual(response.status_code,404)

class ProfileUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.user2 = User.objects.create(username='tester2',email='tester@2.com',password='testthisuseralso')
        self.client = None
        self.request_url = '/Profile/'

    def test_unautherizedEntry(self):
        self.client = Client()
        response = self.client.get(self.request_url+self.user.username+'/')

        self.assertEqual(response.status_code,404)
        # self.assertRedirects(response,expected_url='/Login')

    # def test_unautherizedEntryRandom(self):
    #     self.client = Client()
    #     response = self.client.get(self.request_url+'randomurl')
    #
    #     self.assertEqual(response,302)

    # def test_autherizedIncompleteUserEntry(self):
    #     self.client = Client()
    #     self.client.force_login(self.user2)
    #     response = self.client.get(self.request_url+self.user2.username)
    #
    #     self.assertEqual(response,302)

    # def test_autherizedIncompleteUserEntryRandom(self):
    #     self.client = Client()
    #     self.client.force_login(self.user2)
    #     response = self.client.get(self.request_url+self.user2.username+'randomurl')
    #
    #     self.assertEqual(response.status_code,302)

    def test_autherizedCompleteUserEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url+self.user.username)

        self.assertEqual(response.status_code,200)

    def test_autherizedCompleteUserEntryRandom(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url+'randomurl')

        self.assertEqual(response.status_code,200)

class ChangePasswordUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.user2 = User.objects.create(username='tester2',email='tester@2.com',password='testthisuseralso')
        self.client = None
        self.request_url = '/ChangePassword/'

    def test_unautherizedEntry(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertRedirects(response,expected_url='/Login/')

    def test_unautherizedEntryRandom(self):
        self.client = Client()
        response = self.client.get(self.request_url+'asfd')

        self.assertEqual(response.status_code,404)

    def test_autherizedIncompleteUserEntry(self):
        self.client = Client()
        self.client.force_login(self.user2)
        response = self.client.get(self.request_url)

        self.assertRedirects(response,expected_url='/AddDetails/')

    def test_autherizedIncompleteUserEntryRandom(self):
        self.client = Client()
        self.client.force_login(self.user2)
        response = self.client.get(self.request_url+'randomurl')

        self.assertEqual(response.status_code,404)

    def test_autherizedCompleteUserEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)

    def test_autherizedCompleteUserEntryRandom(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url+'asdlf')

        self.assertEqual(response.status_code,404)

class LoginUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.user2 = User.objects.create(username='tester2',email='tester@2.com',password='testthisuseralso')
        self.client = None
        self.request_url = '/Login/'

    def test_unautherizedEntry(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)

    def test_unautherizedEntryRandom(self):
        self.client = Client()
        response = self.client.get(self.request_url+'asdjflh')

        self.assertEqual(response.status_code,404)

    def test_autherizedEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url)

        self.assertRedirects(response, expected_url='/')

    def test_autherizedEntryRandom(self):
        self.client = Client()
        response = self.client.get(self.request_url+'aksdfkj')

        self.assertEqual(response.status_code,404)

class LogoutUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.user2 = User.objects.create(username='tester2',email='tester@2.com',password='testthisuseralso')
        self.client = None
        self.request_url = '/Logout/'

    def test_autherizedEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url)

        self.assertRedirects(response,expected_url='/')

class RestLoginUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
        user_details = models.User_Profile.objects.create(User=self.user,phone=7894561230,address='Dummy addresss',street='Dummy street',city='Dummy city',pincode=789456)
        self.user.user_profile = user_details
        self.user2 = User.objects.create(username='tester2',email='tester@2.com',password='testthisuseralso')
        self.client = None
        self.request_url = '/Rest_Login/'

    def test_unautherizedEntry(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)

    def test_unautherizedEntryRandom(self):
        self.client = Client()
        response = self.client.get(self.request_url+'asdjflh')

        self.assertEqual(response.status_code,404)

    def test_autherizedEntry(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(self.request_url)

        self.assertRedirects(response, expected_url='/')

    def test_autherizedEntryRandom(self):
        self.client = Client()
        response = self.client.get(self.request_url+'aksdfkj')

        self.assertEqual(response.status_code,404)

class HomeUrlTest(TestCase):
    def setUp(self):
        self.request_url = '/'
        self.client = None

    def test_home(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)

    def test_homeRandom(self):
        self.client = Client()
        response = self.client.get(self.request_url+'asdfjh')

        self.assertEqual(response.status_code,404)
