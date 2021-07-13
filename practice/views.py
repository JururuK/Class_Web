from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from practice.models import NewModel


def practice(review) :

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