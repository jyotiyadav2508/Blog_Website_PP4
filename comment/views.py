from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import CommentForm


def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(
            request, "Comment added successfully!"
        )
        return redirect(reverse("post_detail", args=(post.slug,)))
    else:
        comment_form = CommentForm()
    return render(request, "post_detail.html", {"comment_form": comment_form})


class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit comment
    """
    model = Comment
    template_name = "edit_comment.html"
    form_class = CommentForm
    success_message = "The comment updated successfully!"


@login_required()
def delete_comment(request, comment_id):
    """
    Delete comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, "Comment deleted successfully!")
    return HttpResponseRedirect(
        reverse("post_detail", args=[comment.post.slug])
    )
