from django_summernote.widgets import SummernoteWidget
from .models import Comment
from django import forms


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
