from django.urls import path
from comment.views import CommentCreate,  CommentList, CommentDetail, CommentDelete, edit_comment_view

urlpatterns = [
    path('create_comment/', CommentCreate.as_view()),
    path('comment_list', CommentList.as_view()),
    path('comment_list/<int:id>/', CommentDetail.as_view()),
    path('comment_list/<int:id>/delete/', CommentDelete.as_view()),
    path('comment_list/<int:id>/update/', edit_comment_view),




]