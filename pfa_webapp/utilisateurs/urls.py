from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_utilisateurs, name='index_utilisateurs'),
]
