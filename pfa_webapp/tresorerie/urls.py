from django.urls import path
from . import views

urlpatterns = [
   path('', views.index_tresorerie, name='index_tresorerie')
]