from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_roles, name='index_roles')
]
