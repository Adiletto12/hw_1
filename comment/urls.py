from django.urls import path
from comment.views import create_comment, comment_list_view, comment_detail_view, delete_comment_view, edit_comment_view

urlpatterns = [
    path('create_comment/', create_comment),
    path('comment_list', comment_list_view),
    path('comment_list/<int:id>/', comment_detail_view),
    path('comment_list/<int:id>/delete/', delete_comment_view),
    path('comment_list/<int:id>/update/', edit_comment_view),




]