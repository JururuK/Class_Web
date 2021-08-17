from django.urls import path

from letters.views import CreateLetterView, DetailLetterView

app_name='letter'
urlpatterns = [
    path('upload/',CreateLetterView.as_view(),name='upload'),
    path('detail/<int:pk>',DetailLetterView.as_view(),name='detail'),
]