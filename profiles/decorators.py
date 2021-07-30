from django.http import HttpResponseForbidden

from profiles.models import Profile


def is_profile_owner(func) :
    def decorated(review,*args,**kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])

        if target_profile.user == review.user:
            return func(review,*args,**kwargs)
        else :
            return HttpResponseForbidden()

    return decorated