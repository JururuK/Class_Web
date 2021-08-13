from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from letters.forms import CreateLetterForm
from letters.models import Letter


class CreateLetterView(CreateView):
    model = Letter
    form_class = CreateLetterForm
    success_url = reverse_lazy('article:list')
    template_name = 'letters/upload.html'