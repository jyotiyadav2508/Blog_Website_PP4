from django.test import TestCase
from blog.forms import AddPostForm, UpdatePostForm


class TestForms(TestCase):
    def test_add_post_form_valid_data(self):
        form = AddPostForm(data={
            'title': 'post1',
            'content': 'post content',
            'best_time': 'Jan-mar',
            'ideal_duration': '2days'
        })
        self.assertTrue(form.is_valid())

    def test_add_post_form_no_data(self):
        form = AddPostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_update_post_form_valid_data(self):
        form = UpdatePostForm(data={
            'title': 'post1',
            'content': 'post content',
            'best_time': 'Jan-mar',
            'ideal_duration': '2days'
        })
        self.assertTrue(form.is_valid())

    def test_update_post_form_no_data(self):
        form = UpdatePostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
