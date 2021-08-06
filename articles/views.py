from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from articles.decorators import is_article_owner
from articles.forms import CreateArticleForm
from articles.models import Article

@method_decorator(login_required(login_url=reverse_lazy('practice:login')),'get')
@method_decorator(login_required(login_url=reverse_lazy('practice:login')),'post')
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

@method_decorator(is_article_owner,'get')
@method_decorator(is_article_owner,'post')
class ModifyArticleView(UpdateView):
    model = Article
    form_class = CreateArticleForm
    context_object_name = 'target_article'
    template_name = 'articles/modify.html'

    def get_success_url(self):
        return reverse('article:detail',kwargs={'pk':self.object.pk})

@method_decorator(is_article_owner,'get')
@method_decorator(is_article_owner,'post')
class DeleteArticleView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('article:list')
    template_name = 'articles/delete.html'

class ListArticleView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articles/list.html'
    paginate_by = 15