from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('clients', views.clients, name='clients'),
    path('secret', views.secret, name='secret'),
    path('user', views.user, name='user'),
    path('empty', views.empty, name='empty'),
    path('empty_status', views.empty_status, name='empty_status'),
    path('greetings', views.greetings, name='greetings'),
    path('united_states', views.united_states, name='united_states'),
]
