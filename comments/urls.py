from django.urls import path

from comments.views import CreateCommentView, DeleteCommentView

app_name='comment'

urlpatterns = [
    path('new/',CreateCommentView.as_view(),name='new'),
    path('delete/<int:pk>',DeleteCommentView.as_view(),name='delete'),
]