from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for post comment
    """
    class Meta:
        model = Comment
        fields = ('body',)
