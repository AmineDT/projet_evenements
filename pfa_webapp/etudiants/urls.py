from django.urls import path
from . import views

urlpatterns = [
   path('', views.index_etudiants, name='index_etudiants')
]