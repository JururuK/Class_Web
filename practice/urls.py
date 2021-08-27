from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from practice.views import practice, AccountNew, AccountMyProfile, AccountModify, AccountDelete

app_name = 'practice'



urlpatterns = [
    path('login/', LoginView.as_view(template_name='practice/login.html'),
         name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('new/', AccountNew.as_view(), name = 'new'),
    path('detail/<int:pk>', AccountMyProfile.as_view(), name = 'detail'),
    path('modify/<int:pk>', AccountModify.as_view(), name = 'modify'),
    path('delete/<int:pk>', AccountDelete.as_view(), name = 'delete'),
]