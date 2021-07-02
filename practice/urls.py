from django.urls import path

from practice.views import practice

app_name = 'practice'

urlpatterns = [
    path('exercise/', practice, name='exercise')
]