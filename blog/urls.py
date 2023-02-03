from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('post_detail', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('blog', views.AllBlogPost.as_view(), name='all-blog'),
    path('user_page', views.User.as_view(), name="user-page"),
    path('add_post', views.AddPost.as_view(), name='add-post'),
]
