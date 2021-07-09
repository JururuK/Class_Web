from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def practice(review) :
    if review.method == "POST" :
        return render(review, 'practice/exercise.html',
                      context = {'text':'POST METHOD'})
    else :
        return render(review, 'practice/exercise.html',
                      context = {'text':'GET METHOD!'})