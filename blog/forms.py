from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post
from django import forms
from django.forms import ModelForm


class CommentForm(forms.ModelForm):
    """
    Form for post comment
    """
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Please enter your comment here..',
        'rows': '6',
    }))

    class Meta:
        # Choose fields to display from the Comment model
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    """
    Form to add a blog post
    """
    class Meta:
        model = Post
        fields = (
            'title', 'author', 'destinations',
            'content', 'featured_image', 'best_time',
            'ideal_duration', )

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),  # noqa: E501
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'destinations': forms.Select(attrs={'class': 'form-control'}),
        'content': SummernoteWidget(attrs={'class': 'form-control'}),
        'best_time': forms.TextInput(attrs={'class': 'form-control'}),
        'ideal_duration': forms.TextInput(attrs={'class': 'form-control'}),
    }

