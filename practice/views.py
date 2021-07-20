from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from practice.models import NewModel

def practice(review) :

    if review.method == "POST" :

        temp=review.POST.get('input')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('practice:exercise'))

    else:
        data_list = NewModel.objects.all()
        return render(review, 'practice/exercise.html',
                      context={'data_list': data_list})

class AccountNew(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('practice:exercise')
    template_name = 'practice/new.html'

class AccountMyProfile(DetailView) :
    model = User
    context_object_name = 'target_user'
    template_name = 'practice/detail.html'

class AccountModify(UpdateView) :
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('practice:exercise')
    template_name = 'practice/modify.html'

class AccountDelete(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('practice:login')
    template_name = 'practice/delete.html'