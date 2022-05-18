from django.shortcuts import render

# Create your views here.

def index_etudiants(requests):
    return render(requests, "Index.html")