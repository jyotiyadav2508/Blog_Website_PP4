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
# from blog.views import PostLike, PostDetail
from blog.views import PostLike


def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, 'Comment added successfully. Its awaiting approval')
        # return HttpResponseRedirect(request.path_info)
        return redirect('post_detail', post_id=post_id)
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'comment_form': comment_form})


# def postComment(self, request, slug):
#     """
#     Current user can submit a comment on the post
#     """
#     queryset = Post.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)
#     comments = post.comments.filter(approved=True).order_by("created_on")
#     liked = False
#     if post.likes.filter(id=self.request.user.id).exists():
#         liked = True

#     comment_form = CommentForm(data=request.POST)
#     if comment_form.is_valid():
#         comment_form.instance.email = request.user.email
#         comment_form.instance.name = request.user.username
#         comment = comment_form.save(commit=False)
#         comment.post = post
#         comment.save()
#         messages.success(request, "Thank you for your comment!")
#     else:
#         comment_form = CommentForm()
#     context = {
#             "post": post,
#             "comments": comments,
#             "commented": True,
#             "liked": liked,
#             "comment_form": CommentForm(),
#         }
#     return render(
#         request,
#         "post_detail.html", context
#     )

# def postComment(request):
#     if request.method == "POST":
#         comment = request.POST.get('comment')
#         user = request.user
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comment = Comment(comment=comment, user=user, post=post)
#         comment.save()
#         messages.success(request, "Your comment has been posted successfully")

#     return redirect(f"/blog/{post.slug}")


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
