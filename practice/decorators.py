from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def is_id_owner(func) :
    def decorated(review,*args,**kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user == review.user :
            return func(review,*args,**kwargs)

        else :
            return HttpResponseForbidden()

    return decorated