from django.urls import path
from django.views.generic import TemplateView

from articles.views import CreateArticleView, DetailArticleView, ModifyArticleView, DeleteArticleView, ListArticleView

app_name = 'article'
urlpatterns = [
    path('list/',ListArticleView.as_view(),name='list'),
    path('upload/',CreateArticleView.as_view(),name='upload'),
    path('detail/<int:pk>',DetailArticleView.as_view(),name='detail'),
    path('modify/<int:pk>',ModifyArticleView.as_view(),name='modify'),
    path('delete/<int:pk>',DeleteArticleView.as_view(),name='delete')
]