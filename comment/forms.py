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

    # widgets = {
    #     "body": forms.Textarea(attrs={
    #             "class": "form-control",
    #             "placeholder": "Please enter your comment here..",
    #             "rows": "6",
    #     })}
