from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

from articles.models import Article
from likes.models import LikeRecord


class LikeArticleView(RedirectView):
    def get(self,review,*args,**kwargs):
        user = review.user
        article = Article.objects.get(pk=kwargs['article_pk'])
        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)

        if like_record.exists()
            return HttpResponseRedirect(reverse('article:detail',kwargs={'pk':kwargs['article_pk']}))

        else:
            LikeRecord(user=user,article=article).save()

        article.like += 1
        article.save()

        return super().get(review,*args,**kwargs)

    def get_redirect_url(self,*args,**kwargs):
        return reverse('article:detail',kwargs={'pk':kwargs['article_pk']})
