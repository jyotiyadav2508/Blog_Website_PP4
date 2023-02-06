from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('blog', views.AllBlogPost.as_view(), name='all-blog'),
    path('user_page', views.User.as_view(), name="user-page"),
    # path('add_post', views.AddPost.as_view(), name='add-post'),
    path('add_post', views.user_add_post, name='add-post'),
    path('destinations', views.destinations, name='destinations'),
    path('destinations_post', views.destinations_view, name='destinations-post'),   # noqa: E501
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
