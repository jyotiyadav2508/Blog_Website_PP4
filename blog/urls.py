from . import views
from django.urls import path

urlpatterns = [
    path("", views.AllDestination.as_view(), name="home"),
    path("about", views.about, name="about"),
    path("blog", views.AllBlogPost.as_view(), name="all-blog"),
    path("post_detail/<slug:slug>/", views.postDetail, name="post_detail"),
    path("user_page", views.User.as_view(), name="user-page"),
    path("add_post", views.AddPost.as_view(), name="add-post"),
    path("search", views.search, name="search"),
    path(
        "destinations_post/<str:des>",
        views.destinations_view,
        name="destinations-post",
    ),
    path(
        "user_post_list/", views.UserPostList.as_view(), name="user-post-list"
    ),
    path("like/<slug:slug>/", views.PostLike.as_view(), name="post_like"),
    path("update_post/<slug:slug>/", views.update_post, name="update-post"),
    path(
        "delete_post/<slug:slug>/",
        views.DeletePost.as_view(),
        name="delete-post",
    ),
]
