from django_summernote.widgets import SummernoteWidget
from .models import Post
from django import forms
from django.forms import ModelForm


class AddPostForm(forms.ModelForm):
    """
    Form to add a blog post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "destinations",
            "content",
            "featured_image",
            "best_time",
            "ideal_duration",
        )

    widgets = {
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "author": forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "hidden"
            }
        ),
        "destinations": forms.Select(attrs={"class": "form-control"}),
        "content": SummernoteWidget(
            attrs={
                "class": "form-control",
                "placeholder": "Add your content here",
            }
        ),
        "best_time": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Which season or months",
            }
        ),
        "ideal_duration": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ideal trip duration(days/week)",
            }
        ),
    }


class UpdatePostForm(forms.ModelForm):
    """
    Form to edit a blog post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "destinations",
            "content",
            "featured_image",
            "best_time",
            "ideal_duration",
        )

    widgets = {
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "destinations": forms.Select(attrs={"class": "form-control"}),
        "content": SummernoteWidget(attrs={"class": "form-control"}),
        "best_time": forms.TextInput(attrs={"class": "form-control"}),
        "ideal_duration": forms.TextInput(attrs={"class": "form-control"}),
    }
