from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import CommentForm, AddPostForm


class PostList(generic.ListView):
    """
    Takes the Post Model and makes sure they are approved
    and displaye them on the home page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6


class AllBlogPost(generic.ListView):
    """
    Render the blog page
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = "blog.html"
    paginate_by = 9


class PostDetail(View):
    """
    Render the Post details page of the selected post with approved comments
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Current user can submit a comment on the post
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Thank you for your comment!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """
    When a post is liked/unliked, the slug is noted
    and the like/unlike is counted. Total likes display
    """
    def post(self, request, slug, *args):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'You have unliked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked this post, Thanks!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# @login_required()
# class AddPost(request):
#     """
#     Add a blog post only when user is logged in
#     """
#     if request.method == 'POST':
#         form = PostForm(request.FORM, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.slug = slugify(post.title)
#             form.save()
#             messages.success(
#                 request,
#                 'You have added a new post and it has been flagged for approval!')  # noqa: E501
#             return redirect(reverse('add-post'))
#         else:
#             messages.error(request, 'Failed to Create a post. \
#                             Please ensure the form is valid.')
#     else:
#         form = PostForm()

#     template = 'add_post.html',
#     context = {
#         'form': form,
#     }
#     return render(request, template, context)


class AddPost(LoginRequiredMixin, CreateView):
    """
    Add a blog post only after logged in
    """
    template = 'add_post.html'
    form_class = AddPostForm

    def get_success_url(self):
        """
        Set the reverse url for the sucessfully addition of a post
        """
        return reverse('all-blog')
        # return reverse('list-blog')

    def form_valid(self, form):
        """
        Validate the form and return a success message
        """
        form.instance.author = self.request.user
        messages.success(
            self.request,
            'You have added a post and it has been flagged for approval!')
        form.slug = slugify(form.instance.title)
        return super().form_valid(form)


class User(LoginRequiredMixin, generic.ListView):
    """
    Render the user page
    """
    model = Post
    template_name = "user_page.html"
    # return render(request, 'user_page.html')
