"""New URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articles.views import ListArticleView

urlpatterns = [
    path('',ListArticleView.as_view(),name='main'),
    path('admin/', admin.site.urls), #관리자페이지
    path('practice/', include('practice.urls')),
    path('profiles/', include('profiles.urls')),
    path('articles/', include('articles.urls')),
    path('comments/', include('comments.urls')),
    path('letters/', include('letters.urls')),

    path('subscribes/',include('subscribes.urls')),
    path('likes/',include('likes.urls')),
    path('testapp/',include('testapp.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
