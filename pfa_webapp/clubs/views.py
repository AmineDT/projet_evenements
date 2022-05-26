import sys
from django.shortcuts import render, redirect
import requests
import os
from django.template import RequestContext
from django.contrib import messages
import django_tables2 as tables
from django.views.generic import ListView
from django_tables2 import SingleTableView
from requests import request
from django_tables2.utils import A

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

class ClubTable(tables.Table):
    class Meta:
        model = Club
        template_name = "django_tables2/bootstrap.html"
        fields = ("name_club", "description")


class ClubListView(SingleTableView):
    model = Club
    table_class = ClubTable
    template_name = "Clubs_templates/Clubs_output.html"





