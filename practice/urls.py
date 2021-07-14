from django.urls import path

from practice.views import practice, AccountNew

app_name = 'practice'

urlpatterns = [
    path('exercise/', practice, name='exercise'),
    path('new/', AccountNew.as_view(), name = 'new')
]