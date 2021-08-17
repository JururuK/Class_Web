from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from letters.forms import CreateLetterForm
from letters.models import Letter

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class CreateLetterView(CreateView):
    model = Letter
    form_class = CreateLetterForm
    template_name = 'letters/upload.html'
    def get_success_url(self):
        return reverse('letter:detail',kwargs={'pk':self.object.pk})
class DetailLetterView(DetailView):
    model = Letter
    context_object_name = 'target_letter'
    template_name = 'letters/detail.html'