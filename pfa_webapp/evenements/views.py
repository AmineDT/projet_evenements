from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def index_evenements(requests):
    return render(requests, "Index.html")