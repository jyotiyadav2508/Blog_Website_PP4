from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from blog.models import *
from blog.views import *
from django.urls import reverse, resolve


class TestViews(TestCase):
    """
    Class to test the blog views
    """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test1234"
        )
        Post.objects.create(
            title='title_name',
            author='author_name',
            content='This is post content',
            created_on='Feb. 15, 2023,11:04p.m.',
            best_time='Throughout the year',
            ideal_duration='2-3days',
            destinations='destination_type'
        )
        self.client = Client()

    # def test_add_post_page_GET(self):
    #     response = self.client.get("/add_post")
    #     self.assertEqual(response.status_code, 202)
    #     self.assertTemplateUsed(response, "add_post.html")

    def test_logged_in_user_can_access_user_page(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.get("/user_page")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_page.html")

    def test_loged_in_user_can_access_add_post_page(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.get("/add_post")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_post.html")

    # def test_loged_in_user_can_add_post(self):
    #     self.client.login(username='testuser', password='test1234')
    #     response = self.client.post("/add_post")
    #     self.assertEqual(response.status_code, 200)

    def test_loged_in_user_can_add_post(self):
       

    # def test_loged_in_user_can_update_post(self):
    #     self.client.login(username='testuser', password='test1234')
    #     response = self.client.post("/update_post/<slug:slug>")
    #     self.assertEqual(response.status_code, 200)
