from . import views
from django.urls import path
from .views import AddCommentView

urlpatterns = [
    path('add_comment/<int:pk>', views.AddCommentView.as_view(), name='add_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),   # noqa: E501
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),  # noqa: E501
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('<slug:slug>/', views.PostComment.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
