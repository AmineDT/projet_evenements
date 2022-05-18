from django.shortcuts import render

# Create your views here.

def index_billets(requests):
    return render(requests, "Index.html")