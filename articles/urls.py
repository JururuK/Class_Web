from django.urls import path
from django.views.generic import TemplateView

app_name = 'article'
urlpatterns = [
    path('list/',TemplateView.as_view(template_name='articles/list.html'),name='list')
]