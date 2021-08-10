from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from comments.forms import CreateCommentForm
from comments.models import Comment


class CreateCommentView(CreateView):
    model = Comment
    form_class = CreateCommentForm
    template_name = 'comments/new.html'

    def get_success_url(self):
        return reverse('article:detail', kwargs={'pk': self.object.article.pk})