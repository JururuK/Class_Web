from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from articles.forms import CreateArticleForm
from articles.models import Article


class CreateArticleView(CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = 'articles/upload.html'

    def form_valid(self,form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article:detail',kwargs={'pk':self.object.pk})

class DetailArticleView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articles/detail.html'

class ModifyArticleView(UpdateView):
    model = Article
    form_class = CreateArticleForm
    context_object_name = 'target_article'
    template_name = 'articles/modify.html'

    def get_success_url(self):
        return reverse('article:detail',kwargs={'pk':self.object.pk})

class D