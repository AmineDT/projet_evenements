from django.urls import path
from . import views

urlpatterns = [
   path('', views.index_evenements, name='index_billet')
]