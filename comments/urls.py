from django.urls import path

from comments.views import CreateCommentView

app_name='comment'

urlpatterns = [
    path('new/',CreateCommentView.as_view(),name='new'),
]