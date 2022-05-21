import sys
from django.shortcuts import render
import os



# Create your views here.

def index_labels(requests):
    return render(requests, "Labels_templates/Labels.html")

"""def addlabel(request):
    if request.method == "POST":
        postlabel = Label()
        postlabel.name_label = request.POST.get('name_label')
        postlabel.description = request.POST.get('description_label')
        postlabel.save()
        return render(request, 'Label.html')

    else:
        return render(request, 'Label.html')"""


