from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
class PostModelTest(TestCase):
	
	def setUp(self):
		user1 = User.objects.create(username='testuser1', password='HelloWorld@123', email='testuser1@gmail.com')
		User.objects.create(username='testuser2', password='helloworld@123', email='testuser2@gmail.com')		
		Post.objects.create(
			title='aman',
			slug="aman",
			author=user1,
			body="Hello friends",
			created=datetime.datetime.now(),
		)
	def test_number_of_likes_on_a_post(self):
		user1 = User.objects.get(id=1)
		user2 = User.objects.get(id=2)
		post1 = Post.objects.get(id=1)

		post1.likes.add(user1)
		post1.likes.add(user2)
		self.assertEquals(post1.total_likes(), 2)
	
	def test_get_absolute_url(self):
		post1 = Post.objects.get(id=1)
		self.assertEquals(post1.get_absolute_url(), '/blog/1/aman/')		

	def test_restrict_comment_is_set_to_False(self):
		post1 = Post.objects.get(id=1)
		self.assertEquals(post1.restrict_comment, False)

	def test_status_is_published_or_drafted(self):
		post1 = Post.objects.get(id=1)
		self.assertEquals(post1.status, 'draft')

