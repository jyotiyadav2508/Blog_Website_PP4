# from django.test import TestCase, Client
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from blog.models import *
# from blog.views import *
# from django.urls import reverse, resolve
# # import requests


# class TestUrls(TestCase):
#     """
#     Class to test the blog views
#     """
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username="testuser", password="test1234"
#         )
#         self.client = Client()

#     def test_home_page(self):
#         url = reverse('home')
#         self.assertEqual(resolve(url).func.view_class, AllDestination)

#     def test_blog_page(self):
#         url = reverse('all-blog')
#         self.assertEqual(resolve(url).func.view_class, AllBlogPost)

#     def test_about_page(self):
#         response = self.client.get("/about")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "about.html")

#     def test_destinations_post_page(self):
#         response = self.client.get("/destinations_post/<str:des>")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "destinations_post.html")

#     def test_post_detail_page(self):
#         url = reverse('post_detail', args=['some-slug'])
#         self.assertEqual(resolve(url).func, postDetail)

#     def test_search_page(self):
#         url = reverse('search')
#         self.assertEqual(resolve(url).func, search)

#     def test_logged_in_user_can_access_user_page(self):
#         self.client.login(username='testuser', password='test1234')
#         response = self.client.get("/user_page")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "user_page.html")

#     def test_loged_in_user_can_access_add_post_page(self):
#         self.client.login(username='testuser', password='test1234')
#         response = self.client.get("/add_post")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "add_post.html")

#     def test_loged_in_user_can_add_post(self):
#         self.client.login(username='testuser', password='test1234')
#         response = self.client.post("/add_post")
#         self.assertEqual(response.status_code, 200)

#     def test_loged_in_user_can_update_post(self):
#         url = reverse('update-post', args=['some-slug'])
#         self.assertEqual(resolve(url).func, update_post)

#     def test_loged_in_user_can_like_post(self):
#         url = reverse('post_like', args=['some-slug'])
#         self.assertEqual(resolve(url).func.view_class, PostLike)

#     def test_loged_in_user_can_delete_post(self):
#         url = reverse('delete-post', args=['some-slug'])
#         self.assertEqual(resolve(url).func.view_class, DeletePost)
