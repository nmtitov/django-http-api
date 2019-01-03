from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('items', views.items, name='items'),
    path('settings', views.settings, name='settings'),
]
