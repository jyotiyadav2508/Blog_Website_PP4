from django.contrib import admin
from .models import Post, Comment, Destination, Author
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add fields which will use summernote editor in admin panel
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'destinations']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for comments in admin panel
    """
    list_display = ('name', 'body', 'email', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    """
    Add fields for destination in admin panel
    """
    list_display = ['title']
    search_fields = ['title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Add fields for author in admin panel
    """
    list_display = ('user', 'created_on')
    search_fields = ['user']
