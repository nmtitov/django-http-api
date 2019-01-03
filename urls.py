from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counterparties', views.counterparties, name='counterparties'),
    path('items', views.items, name='items'),
    path('settings', views.settings, name='settings'),
]
