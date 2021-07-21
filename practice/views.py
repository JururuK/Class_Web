from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from practice.forms import AccountModifyForm
from practice.models import NewModel

def practice(review) :
    if review.user.is_authenticated:

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

    else :
        return HttpResponseRedirect(reverse('practice:login'))

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
    form_class = AccountModifyForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('practice:exercise')
    template_name = 'practice/modify.html'

    def get(self,review,*args,**kwargs):
        if review.user.is_authenticated and self.get_object() == review.user:
            return super().get(review,*args,**kwargs)
        else:
            return HttpResponseForbidden()

    def post(self,review,*args,**kwargs) :
        if review.user.is_authenticated and self.get_object() == review.user:
            return super().post(review,*args,**kwargs)
        else:
            return HttpResponseForbidden()

class AccountDelete(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('practice:login')
    template_name = 'practice/delete.html'

    def get(self,review,*args,**kwargs):
        if review.user.is_authenticated and self.get_object() == review.user:
            return super().get(review,*args,**kwargs)
        else:
            return HttpResponseForbidden()

    def post(self,review,*args,**kwargs) :
        if review.user.is_authenticated and self.get_object() == review.user:
            return super().post(review,*args,**kwargs)
        else:
            return HttpResponseForbidden()