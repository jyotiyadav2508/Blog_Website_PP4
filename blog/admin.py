from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add fields which will use summernote editor in admin panel
    """
    summernote_fields = ('content')
