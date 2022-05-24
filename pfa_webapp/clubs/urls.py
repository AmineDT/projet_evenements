from django.urls import path
from . import views

urlpatterns = [
   path('', views.index_clubs, name='index_clubs')
]