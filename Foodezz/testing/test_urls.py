from django.test import Client, TestCase
from django.contrib.auth.models import User
from payments.models import *
from django.utils import timezone

class RegisterTest(TestCase):
    def setUp(self):
        c = Client()

    def test_anonymous_ping(self):
        response = self.client.get('/Register/')

        self.assertEqual(response.status_code, 200)

class RegisterUrlTest(TestCase):

    def setUp(self):
        self.createduser = User.objects.create_user(username="testnormaluser", email="testnormaluser@ts.com",
                                                    password="Test Hello World")
        self.client = None
        self.request_url = '/Register/'

    def test_anonymous_ping(self):
        self.client = Client()
        response = self.client.get(self.request_url)

        self.assertEqual(response.status_code,200)

    def test_authenticated_ping(self):
        self.client = Client()
        self.client.force_login(self.createduser)
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 302)

    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createduser)
        response = self.client.get('/Register/blahblah')
        self.assertEqual(response.status_code, 404)




class LoginUrlTest(TestCase):

    def setUp(self):
        self.createduser = User.objects.create_user(username="testnormaluser", email="testnormaluser@ts.com",
                                                    password="Test Hello World")
        self.client = None
        self.request_url = '/Login/'
        # Create clients on the fly in the tests as login/logout is required

    def test_anonymous_ping(self):
        self.client = Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)

    def test_authenticated_ping(self):
        self.client = Client()
        self.client.force_login(self.createduser)
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 302)

    def test_authenticated_random_id_ping(self):
        self.client = Client()
        self.client.force_login(self.createduser)
        response = self.client.get('registration/login/blahblah')
        self.assertEqual(response.status_code, 404)


class BlankUrlTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_anonymous_ping(self):
        response = self.client.get('')

        self.assertEqual(response.status_code, 200)


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_anonymous_ping(self):
        response = self.client.get('/blog/')

        self.assertEqual(response.status_code, 200)

# class MakeOrderConfirmationTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='testuser',email='testuser@tests.com',password='Test this password')
#
#         self.client = Client()
#         self.request_url = '/payments/makeorderconfirm/'
#
#     def test_anonymous_ping(self):
#         response = self.client.get(self.request_url)
#         self.assertEqual(response.status_code, 301)
#
#     def test_unautherizedEntry(self):
#         self.client = Client()
#         response = self.client.get(self.request_url)
#         self.assertEqual(response.status_code, 200)
#     #
#     # def test_autherizedEntry(self):
#     #     self.client = Client()
#     #     self.client.force_login(self.user)
#     #     response = self.client.get(self.request_url)
#     #     self.assertRedirects(response, expected_url='/')


class LocateRestaurentsTest(TestCase):
    def setUp(self):
        self.client = Client()
        RestaurantLog.objects.create(
            name='aman',
            phone='1234567890',
            address='keshav',
            street='54',
            city='tada',
            pincode='123456',
            restimage='static/images/123.png'
            )
    def test_anonymous_ping(self):
        restaurent_instance = RestaurantLog.objects.get(id=1)
        response = self.client.get('/payments/locaterestaurants/'+restaurent_instance.city)
        print(response)
        self.assertEqual(response.status_code, 200)


class OrderConfirm(TestCase):
    def setUp(self):
        self.client = Client()
        RestaurantLog.objects.create(
        name='aman',
        phone='1234567890',
        address='keshav',
        street='54',
        city='tada',
        pincode='123456',
        restimage='static/images/123.png'
        )

        User.objects.create_user(username="testnormaluser", email="testnormaluser@ts.com",
        password="Test Hello World")
        
        Orders.objects.create(
            orderid='1',
            customerid=User.objects.get(id=1),
            restaurantid=RestaurantLog.objects.get(id=1),
            deliveryid='1',
            foodname='veg',
            quantity='4',
            price='32',
        )
       
    def test_authenticated_ping(self):
        self.client = Client()
        user1 = User.objects.get(id=1)
        response = self.client.get('/Login/')
        self.assertEqual(response.status_code, 200)

    # def test_anonymous_ping(self):
    #     orderId = Orders.objects.get(id=1)
    #     user1 = User.objects.get(id=1)
    #     response = self.client.get('/payments/makeorderconfirm/')
    #
    #     self.assertRedirects(response, expected_url='/Login/?next=/payments/makeorderconfirm/')


# class paymentTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         RestaurantLog.objects.create(
#             name='aman',
#             phone='1234567890',
#             address='keshav',
#             street='54',
#             city='tada',
#             pincode='123456',
#             restimage='static/images/123.png'
#         )
#
#         User.objects.create_user(username="testnormaluser", email="testnormaluser@ts.com",
#                                  password="Test Hello World")
#
#         Orders.objects.create(
#             orderid='1',
#             customerid=User.objects.get(id=1),
#             restaurantid=RestaurantLog.objects.get(id=1),
#             deliveryid='1',
#             foodname='veg',
#             quantity='4',
#             price='32',
#         )
#
#         RestaurantItems.objects.create(
#             restaurantid=RestaurantLog.objects.get(id=1),
#             foodname='Test biryani',
#             type="veg",
#             category="main_course",
#             availability="50",
#             price="10",
#             foodimage='static/images/123.png'
#         )
#
#     def test_authenticated_ping(self):
#         self.client = Client()
#         user1 = User.objects.get(id=1)
#         response = self.client.get('/Login/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_anonymous_ping(self):
#         orderId = Orders.objects.get(id=1)
#         user1 = User.objects.get(id=1)
#         response = self.client.get('/payments/search/')
#
#         self.assertRedirects(response, expected_url='/Login/?next=/payments/pay')
