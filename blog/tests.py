from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.models import *
from blog.views import *
from django.urls import reverse
# Create your tests here.


class TestModels(TestCase):
    """
    Class to test the blog models
    """
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', password='test1234'
        )

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_get_sucess_url(self):
        add_post = AddPost.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(add_post.get_sucess_url(), '/blog/add_post/1')
