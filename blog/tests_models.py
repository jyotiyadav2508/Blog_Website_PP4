from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Destination


class TestModels(TestCase):
    """
    Class to test model
    """
    def setUp(self):
        self.test_user = User.objects.create(
            password='test123', username='testuser')

    def test_destination_model_str(self):
        destination = Destination(title='my destination')
        destination.save()

        self.assertEqual(str(destination), destination.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(
            Destination._meta.verbose_name_plural), "Destinations")
