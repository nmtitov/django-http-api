from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.clients, name='clients'),
    path('secret', views.secret, name='secret'),
    path('user', views.user, name='user'),
]
