from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def practice(review) :
    return render(review, 'practice/exercise.html')