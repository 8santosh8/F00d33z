from django.test import TestCase
from django.urls import reverse
from blog.models import *
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
class post_list_view_test(TestCase):
	@classmethod
	def setUpTestData(cls):
		#Create 10 posts for pagination tests
		number_of_posts = 13
		user1 = User.objects.create(username='testuser1', password='HelloWorld@123', email='testuser1@gmail.com')
		for posts in range(number_of_posts):
			Post.objects.create(
				title='aman',
				slug="aman",
				author=user1,
				body="Hello friends",
				created=timezone.now(),
			)
	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/blog/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.client.get('/blog/')
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get('/blog/')
		self.assertTemplateUsed(response, 'blog/post_list.html')

	def test_pagination_is_ten(self):
		response = self.client.get('/blog/')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('page_range' in response.context)
		self.assertFalse(response.context['page_range'] == True)
		self.assertFalse(len(response.context['posts']) == 10)

	def tests_lists_all_posts(self):
		#Get second page and confirm it has exactly 3 remaining items
		response = self.client.get('/blog/'+'?page=2')
		self.assertEqual(response.status_code, 200)
		self.assertTrue('page_range' in response.context)
		self.assertFalse(response.context['page_range'] == True)
		self.assertFalse(len(response.context['posts']) == 2)

class likes_post_by_only_logged_in_user(TestCase):
	def setUp(self):
		#Create two users
		test_user1 = User.objects.create(username='testuser1', password='HelloWorld@123', email='testuser1@gmail.com')
		test_user2 = User.objects.create(username='testuser2', password='helloWorld@123', email='testuser2@gmail.com')
		test_user1.save()
		test_user2.save()

		#Create a post
		Post.objects.create(
			title='aman',
			slug="aman",
			author=test_user1,
			body="Hello friends",
			created=timezone.now(),
		)
	def test_logged_in_users_correct_template(self):
		login = self.client.login(username='testuser1', password='HelloWorld@123')
		response = self.client.get('/blog/1/aman/')
	
		#check that we got a success redirect response
		self.assertEqual(response.status_code, 200)
