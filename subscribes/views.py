from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from letters.models import Letter
from subscribes.models import Subscription


@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):

    def get(self,review,*args,**kwargs):
        user = review.user
        letter = Letter.objects.get(pk=kwargs['letter_pk'])
        subscription = Subscription.objects.filter(user=user,
                                                   letter=letter)
        if subscription.exists():
            subscription.delete()
        else :
            Subscription(user=user,letter=letter).save()
        return super().get(review,*args,**kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('letter:detail',kwargs={'pk':kwargs['letter_pk']})