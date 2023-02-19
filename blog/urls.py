from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.AllDestination.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('blog', views.AllBlogPost.as_view(), name='all-blog'),
    path('user_page', views.User.as_view(), name="user-page"),
    path('add_post', views.AddPost.as_view(), name='add-post'),
    path('user_post_list/', views.UserPostList.as_view(), name='user-post-list'),   # noqa: E501
    path("search", views.search, name='search'),
    # path('destinations', views.destinations, name='destinations'),
    # path('', views.destinations, name='home'),
    path('destinations_post/<str:des>', views.destinations_view, name='destinations-post'),   # noqa: E501
    # path('destinations_post/<str:des>', views.DestinationListView.as_view(), name='destinations-post'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),  # noqa: E501
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('update_post/<slug:slug>/', views.update_post, name='update-post'),
    path('delete_post/<slug:slug>/', views.DeletePost.as_view(), name='delete-post'),  # noqa: E501
]
