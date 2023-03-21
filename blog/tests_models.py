from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Destination, Post, Author


class TestModels(TestCase):
    """
    Class to test model
    """
    def setUp(self):
        self.test_user = User.objects.create(
            password='test123', username='testuser'
        )

    def test_destination_model_str(self):
        destination = Destination(title='my destination')
        destination.save()

        self.assertEqual(str(destination), destination.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(
            Destination._meta.verbose_name_plural), "Destinations")

    # def test_str_method_returns_number_of_likes(self):
    #     self.post = Post.objects.create(title='Test Post')
    #     self.post.likes = 5
    #     self.post.save()

    #     self.assertEqual(str(self.post), 'Test Post (5 likes)')
