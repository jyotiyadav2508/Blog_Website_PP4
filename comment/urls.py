from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path("add_comment/<int:post_id>", views.add_comment, name="add_comment"),
    path(
        "edit_comment/<int:pk>",
        views.EditComment.as_view(),
        name="edit_comment",
    ),
    path(
        "delete_comment/<int:comment_id>",
        views.delete_comment,
        name="delete_comment",
    ),
]
