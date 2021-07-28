from django.urls import path

from profiles.views import ProfileCreateView, ProfileUpdateView

app_name = 'profile'
urlpatterns = [
    path('new/',ProfileCreateView.as_view(),name='new'),
    path('modify/<int:pk>',ProfileUpdateView.as_view(),name='modify')
]