from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Destination(models.Model):
    """
    Model for destination place
    """
    title = models.CharField(max_length=100, blank=True)
    destination_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=100, unique=True, default="", null=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Model for Author
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.OneToOneField(Author, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default="", unique=True)
    approved = models.BooleanField(default=False)
    author_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    """
    Model for main blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    # author = models.ForeignKey(
    #     Author, on_delete=models.CASCADE, related_name="blog_posts")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="blogpost_likes", blank=True)
    comment_count = models.IntegerField(default=0)
    best_time = models.CharField(max_length=100)
    ideal_duration = models.TextField(
        verbose_name="Ideal trip duration (days)")
    destinations = models.ManyToManyField(Destination, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()


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



