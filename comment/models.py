from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse
from blog.models import Post

STATUS = ((0, "Draft"), (1, "Published"))


class Comment(models.Model):
    """
    Model for comment
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models. CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        To order the comments on the created_on field in the ascending order
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('post_detail', args=[self.post.slug])
