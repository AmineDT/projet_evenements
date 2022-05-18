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
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('billets/', include('billets.urls')),
    path('etudiants/', include('etudiants.urls')),
    path('evenements/', include('evenements.urls')),
    path('labels/', include('labels.urls')),
    path('membres/', include('membres.urls')),
    path('roles/', include('roles.urls')),
    path('tresorerie/', include('tresorerie.urls')),
    path('utilisateurs/', include('utilisateurs.urls')),


]
