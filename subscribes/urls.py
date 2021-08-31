from django.urls import path

from subscribes.views import SubscriptionView, SubscriptionListView

app_name='subscribe'
urlpatterns = [
    path('subscribe/<int:letter_pk>',SubscriptionView.as_view(),name='subscribe'),
    path('list/',SubscriptionListView.as_view(),name='list')
]