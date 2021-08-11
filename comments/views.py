from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from comments.decorators import is_comment_owner
from comments.forms import CreateCommentForm
from comments.models import Comment

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class CreateCommentView(CreateView):
    model = Comment
    form_class = CreateCommentForm
    template_name = 'comments/new.html'

    def form_valid(self,form):
        form.instance.writer=self.request.user
        form.instance.article_id=self.request.POST.get('article_pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk': self.object.article.pk})

@method_decorator(is_comment_owner,'get')
@method_decorator(is_comment_owner,'post')
class DeleteCommentView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'comments/delete.html'
    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk': self.object.article.pk})
