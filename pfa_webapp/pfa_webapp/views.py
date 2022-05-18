from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Index.html')

def contact(request):
    return render(request, 'Contact.html')

def about(request):
    return render(request, 'About.html')