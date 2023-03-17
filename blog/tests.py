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

    def test_user_page(self):
        self.login()
        response = self.client.get("/user_page/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_page.html")

    # def test_get_sucess_url(self, request):
    #     # add_post = AddPost.get(f'/add-post/{post.id}')
    #     response = self.client.get(f'/add_post/{post.id}')
    #     self.assertEqual(add_post.get_sucess_url(), "/blog/add_post/1")
