from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from practice.views import practice, AccountNew

app_name = 'practice'

urlpatterns = [
    path('exercise/', practice, name='exercise'),
    path('login/', LoginView.as_view(template_name='practice/login.html'),
         name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('new/', AccountNew.as_view(), name = 'new')
]