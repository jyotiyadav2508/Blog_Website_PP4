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
        # post = Post.objects.create(
        #     title='Test post',
        #     content='This is post content',
        #     created_on='Feb.15,2023,11:04p.m.',
        #     best_time='Throughout the year',
        #     ideal_duration='2-3days',
        # )
        self.client = Client()

    # def test_add_post_page_GET(self):
    #     response = self.client.get("/add_post")
    #     self.assertEqual(response.status_code, 202)
    #     self.assertTemplateUsed(response, "add_post.html")


    # def test_loged_in_user_can_add_post(self):
    #     self.client.login(username='testuser', password='test1234')
    #     response = self.client.post("/add_post")
    #     self.assertEqual(response.status_code, 200)
        # self.assertEqual(Post.objects.count(), 1)

    # def test_loged_in_user_can_add_post(self):
       

    # def test_loged_in_user_can_update_post(self):
        # post = Post.objects.create(
        #     title='Test post',
        #     content='This is post content',
        #     created_on='Feb.15,2023,11:04p.m.',
        #     best_time='Throughout the year',
        #     ideal_duration='2-3days',
        # )
        # self.client.login(username='testuser', password='test1234')
        # response = self.client.get(f'/update_post/<slug:slug>/{post.slug}')
        # self.assertEqual(response.status_code, 200)

    
    # def test_AddPost_view(self):
    #     self.add_post_url = reverse('add-post')
    #     self.post_data = {
    #         'title': 'Test Post',
    #         'body': 'This is a test post',
    #         'author': 'Test Author'
    #     }
    #     response = self.client.post(self.add_post_url, self.post_data)
    #     self.assertEqual(response.status_code, 302) # check if redirecting
    #     self.assertEqual(Post.objects.count(), 1) # check if post created
    #     post = Post.objects.first()
    #     self.assertEqual(post.title, 'Test Post') # check if title is correct
    #     self.assertEqual(post.body, 'This is a test post') # check if body is correct
    #     self.assertEqual(post.author, 'Test Author')
