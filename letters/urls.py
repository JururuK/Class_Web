from django.urls import path

from letters.views import CreateLetterView
app_name='letter'
urlpatterns = [
    path('upload/',CreateLetterView.as_view(),name='upload')
]