from . import views
from django.urls import path

urlpatterns = [
    path('edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),   # noqa: E501
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),  # noqa: E501
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
