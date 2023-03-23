from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import AddPostForm, UpdatePostForm
from comment.forms import CommentForm
from comment.models import Comment


class AllDestination(generic.ListView):
    """
    Render the all destinations type on home page
    """
    model = Destination
    template_name = "index.html"


class AllBlogPost(generic.ListView):
    """
    Render the blog page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 9


def postDetail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "user": request.user,
        "comment_form": CommentForm(),
    }
    return render(request, "post_detail.html", context)


class PostLike(View):
    """
    When a post is liked/unliked, the slug is noted
    and the like/unlike is counted. Total likes display
    """

    def post(self, request, slug, *args):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, "You have unliked this post.")
        else:
            post.likes.add(request.user)
            messages.success(request, "You have liked this post, Thanks!")
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add a blog post only when user is logged in
    """
    model = Post
    form_class = AddPostForm
    template_name = "add_post.html"
    success_message = "You have added a new post, It's awaiting approval!"

    def get_success_url(self):
        """
        Set the reverse url for the successful addition
        of the post to the database
        """
        return reverse("user-page")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.slug = slugify(form.instance.title)
        return super().form_valid(form)


class UserPostList(LoginRequiredMixin, generic.ListView):
    """
    Display all posts of a particular logged in user in one place
    """
    model = Post
    author = Post.author
    template_name = "user_post_list.html"

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(
            author=self.request.user, status=1).order_by(
            "-created_on"
        )


@login_required()
def update_post(request, slug):
    """
    Users can update their blog post that they have created
    """
    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        if request.method == "POST":
            form = UpdatePostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.status = 1
                form.save()
                messages.success(request, "Your post updated successfully!")
                return redirect(reverse("user-post-list"))
            else:
                messages.error(request, "Failed to update the post.")
        else:
            form = UpdatePostForm(instance=post)
    else:
        messages.error(request, "Sorry, This is not your post.")

    template = ("update_post.html",)
    context = {"form": form, "post": post}
    return render(request, template, context)


class DeletePost(generic.DeleteView):
    """
    Class to allow to delete a post
    """
    model = Post
    template_name = "delete_post.html"
    success_message = "Post was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Set the reverse url for the successful delete
        of the post to the database
        """
        return reverse("user-post-list")


def about(request):
    """
    Render the about page
    """
    return render(request, "about.html")


class User(LoginRequiredMixin, generic.ListView):
    """
    Render the user page
    """
    model = Post
    template_name = "user_page.html"


def destinations_view(request, des):
    """
    Render the posts for selected destination
    """
    destinations_post = Post.objects.filter(
        destinations__title__contains=des, status=1
    )
    return render(
        request,
        "destinations_post.html",
        {"des": des.title(), "destinations_post": destinations_post},
    )


def destinations_list(request):
    """Return a list of destinations for the dropdown in the navbar"""
    destinations_list = Destination.objects.all()
    context = {
        "destinations_list": destinations_list,
    }
    return context


def search(request):
    """
    To search for a blog post
    """
    q = request.GET.get("q")
    results = []

    if "q" in request.GET:
        results = Post.objects.filter(
            Q(title__icontains=q) | Q(content__icontains=q)
        ).filter(
            status=1
        )  # noqa: E501

    return render(request, "search.html", {"q": q, "results": results})
