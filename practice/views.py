from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from practice.models import NewModel


def practice(review) :

    if review.method == "POST" :

        temp=review.POST.get('input')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()
        return render(review, 'practice/exercise.html',
                      context = {'model_instance':model_instance})
    else :
        return render(review, 'practice/exercise.html',
                      context = {'text':'아직은 GET'})