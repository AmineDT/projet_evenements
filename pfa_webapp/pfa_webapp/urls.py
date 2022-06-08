"""pfa_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name="urladmin"),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),
    path('', views.index, name="index"),
    path('billets/', include('billets.urls'), name="billets"),
    path('etudiants/', include('etudiants.urls'), name="etudiants"),
    path('evenements/', include('evenements.urls'), name="evenements"),
    path('clubs/', include('clubs.urls'), name="clubs"),
    path('membres/', include('membres.urls'), name="membres"),
    path('roles/', include('roles.urls'), name="roles"),
    path('achats/', include('achats.urls'), name="tresorerie"),
    path('utilisateurs/', include('utilisateurs.urls'), name="utilisateurs"),
    path('tresorerie/', views.tresorerie, name="tresorerie"),
    path('tresorerie_club/', views.tresorerie_club, name="tresorerie_club"),


]
