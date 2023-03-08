from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import CommentForm
from blog.views import PostLike, PostDetail


class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit comment
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = "The comment updated successfully!"


@login_required()
def delete_comment(request, comment_id):
    """
    Delete comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    return HttpResponseRedirect(reverse(
        'post_detail', args=[comment.post.slug]))
