from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_membres, name='index_membres')
]
