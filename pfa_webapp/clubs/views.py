import sys
from django.shortcuts import render, redirect
import requests
import os
from django.template import RequestContext
from django.contrib import messages
from .models import Club
# Create your views here.


def index_clubs(request):
    if request.method == "POST":
        name_club = request.POST['name_club']
        description = request.POST['description']
        data = Club(name_club=name_club, description=description)
        data.save()
        messages.success(request, 'Club ajouté avec succès.')

        return render(request, 'Clubs_templates/Clubs.html')
    else:
        return render(request, 'Clubs_templates/Clubs.html')


