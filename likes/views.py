from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articles.models import Article
from likes.models import LikeRecord

@method_decorator(login_required(login_url=reverse_lazy('practice:login')),'get')
class LikeArticleView(RedirectView):
    def get(self,review,*args,**kwargs):
        user = review.user
        article = Article.objects.get(pk=kwargs['article_pk'])
        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)

        if like_record.exists():
            return HttpResponseRedirect(reverse('article:detail',kwargs={'pk':kwargs['article_pk']}))

        else:
            LikeRecord(user=user,article=article).save()

        article.like += 1
        article.save()

        return super().get(review,*args,**kwargs)

    def get_redirect_url(self,*args,**kwargs):
        return reverse('article:detail',kwargs={'pk':kwargs['article_pk']})
