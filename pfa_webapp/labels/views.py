import sys
from django.shortcuts import render, redirect
import requests
import os
from django.template import RequestContext
from django.contrib import messages
from .models import Label
# Create your views here.


def index_labels(request):
    if request.method == "POST":
        name_label = request.POST['name_label']
        description = request.POST['description']
        data = Label(name_label=name_label, description=description)
        data.save()
        messages.success(request, 'Label ajouté avec succès.')

        return render(request, 'Labels_templates/Labels.html')
    else:
        return render(request, 'Labels_templates/Labels.html')

