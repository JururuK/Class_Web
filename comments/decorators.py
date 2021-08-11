from django.http import HttpResponseForbidden

from comments.models import Comment


def is_comment_owner(func):
    def decorated(review,*args,**kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == review.user:
            return func(review,*args,**kwargs)

        else :
            return HttpResponseForbidden()

    return decorated