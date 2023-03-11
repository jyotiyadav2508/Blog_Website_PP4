from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import *


class TestModels(TestCase):
    """
    Class to test the blog models
    """
    def setUp(self):
        self.test_user = User.objects.create(
            username='testuser', password='test1234'
        )

    def test_post_model_str(self):
        post = Post.objects.create(title="title", author=self.test_user)
        self.assertEqual((str(post.title)), 'title')
        self.assertEqual((str(post.author)), 'testuser')
