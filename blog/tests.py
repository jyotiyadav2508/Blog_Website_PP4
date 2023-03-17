from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from blog.models import *
from blog.views import *
from django.urls import reverse


class TestViews(TestCase):
    """
    Class to test the blog views
    """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test1234"
        )

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_blog_page(self):
        response = self.client.get("/blog")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog.html")
