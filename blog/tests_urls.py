from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from blog.models import *
from blog.views import *
from django.urls import reverse, resolve


class TestUrls(TestCase):
    """
    Class to test the blog urls
    """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test1234"
        )
        self.client = Client()

    def test_home_page_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, AllDestination)

    def test_blog_page_url(self):
        url = reverse('all-blog')
        self.assertEqual(resolve(url).func.view_class, AllBlogPost)

    def test_about_page_url(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_destinations_post_page_url(self):
        url = reverse('destinations-post', args=['some-str'])
        self.assertEqual(resolve(url).func, destinations_view)

    def test_post_detail_page_url(self):
        url = reverse('post_detail', args=['some-slug'])
        self.assertEqual(resolve(url).func, postDetail)

    def test_search_page_url(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)

    def test_logged_in_user_can_access_user_page_url(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.get("/user_page")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_page.html")

    def test_loged_in_user_can_access_add_post_page_url(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.get("/add_post")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_post.html")

    def test_loged_in_user_can_add_post_url(self):
        self.client.login(username='testuser', password='test1234')
        response = self.client.post("/add_post")
        self.assertEqual(response.status_code, 200)

    def test_loged_in_user_can_update_post_url(self):
        url = reverse('update-post', args=['some-slug'])
        self.assertEqual(resolve(url).func, update_post)

    def test_loged_in_user_can_like_post(self):
        url = reverse('post_like', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, PostLike)

    def test_loged_in_user_can_delete_post(self):
        url = reverse('delete-post', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, DeletePost)
