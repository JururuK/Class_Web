from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from comments.forms import CreateCommentForm
from comments.models import Comment


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

class DeleteCommentView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'comments/delete.html'
    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk': self.object.article.pk})
