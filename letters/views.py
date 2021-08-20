from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articles.models import Article
from letters.forms import CreateLetterForm
from letters.models import Letter
from subscribes.models import Subscription


@method_decorator(login_required(login_url=reverse_lazy('practice:login')),'get')
@method_decorator(login_required(login_url=reverse_lazy('practice:login')),'post')
class CreateLetterView(CreateView):
    model = Letter
    form_class = CreateLetterForm
    template_name = 'letters/upload.html'
    def get_success_url(self):
        return reverse('letter:detail',kwargs={'pk':self.object.pk})
class DetailLetterView(DetailView,MultipleObjectMixin):
    model = Letter
    context_object_name = 'target_letter'
    template_name = 'letters/detail.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        user = self.request.user
        letter = self.object

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                      letter=letter)
        else:
            subscription = None
        article_list = Article.objects.filter(letter=self.object)
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,
                                        **kwargs)
class ListLetterView(ListView):
    model = Letter
    context_object_name = 'letter_list'
    template_name = 'letters/list.html'
    paginate_by = 10