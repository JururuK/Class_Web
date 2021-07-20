from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from practice.views import practice, AccountNew, AccountMyProfile, AccountModify

app_name = 'practice'



urlpatterns = [
    path('exercise/', practice, name='exercise'),
    path('login/', LoginView.as_view(template_name='practice/login.html'),
         name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('new/', AccountNew.as_view(), name = 'new'),
    path('detail/<int:pk>', AccountMyProfile.as_view(), name = 'detail'),
    path('modify/<int:pk>', AccountModify.as_view(), name = 'modify')
]