from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articles.models import Article
from practice.decorators import is_id_owner
from practice.forms import AccountModifyForm
from practice.models import NewModel

@login_required(login_url=reverse_lazy('practice:login'))
def practice(review) :
    if review.user.is_authenticated:

        if review.method == "POST" :

            temp=review.POST.get('input')

            model_instance = NewModel()
            model_instance.text = temp
            model_instance.save()

            return HttpResponseRedirect(reverse('article:lists'))

        else:
            data_list = NewModel.objects.all()
            return render(review, 'articles/list.html',
                          context={'data_list': data_list})

    else :
        return HttpResponseRedirect(reverse('practice:login'))

class AccountNew(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('practice:exercise')
    template_name = 'practice/new.html'

class AccountMyProfile(DetailView,MultipleObjectMixin) :
    model = User
    context_object_name = 'target_user'
    template_name = 'practice/detail.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        article_list=Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,**kwargs)

id_owner = [login_required,is_id_owner]
@method_decorator(id_owner,'get')
@method_decorator(id_owner,'post')
class AccountModify(UpdateView) :
    model = User
    form_class = AccountModifyForm
    context_object_name = 'target_user'
    template_name = 'practice/modify.html'

    def get_success_url(self):
        return reverse('practice:detail',kwargs={'pk':self.object.pk})

id_owner = [login_required,is_id_owner]
@method_decorator(id_owner,'get')
@method_decorator(id_owner,'post')
class AccountDelete(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('practice:login')
    template_name = 'practice/delete.html'
