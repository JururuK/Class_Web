from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articles.forms import CreateArticleForm
from articles.models import Article


class CreateArticleView(CreateView):
    model = Article
    form_class = CreateArticleForm
    success_url = reverse_lazy('practice:exercise')
    template_name = 'articles/upload.html'

    def form_valid(self,form):
        form.instance.writer = self.request.user
        return super().form_valid(form)