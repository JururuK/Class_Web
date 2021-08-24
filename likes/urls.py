from django.urls import path

from likes.views import LikeArticleView
app_name = 'like'
urlpatterns = [
    path('article/<int:article_pk>',LikeArticleView.as_view(),name='article_like'),
]