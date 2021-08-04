from django.http import HttpResponseForbidden

from articles.models import Article


def is_article_owner(func):
    def decorated(review,*args,**kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.writer == review.user :
            return func(review,*args,**kwargs)

        else : return HttpResponseForbidden()
    return decorated