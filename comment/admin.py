from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for comments in admin panel
    """
    list_display = ("name", "body", "email", "post", "created_on")
    search_fields = ["name", "email", "body"]
    list_filter = ("created_on",)
