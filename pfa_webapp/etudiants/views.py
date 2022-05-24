import sys
from django.shortcuts import render, redirect
import requests
import os
from django.template import RequestContext
from django.contrib import messages
from .models import Students


# Create your views here.


def index_etudiants(request):
    if request.method == "POST":
        name_student = request.POST.get('name_student')
        surname_student = request.POST['surname_student']
        study_field = request.POST['study_field']
        email = request.POST['email']
        phone = request.POST['phone']
        data = Students(name_student=name_student, surname_student=surname_student, study_field=study_field,
                        email=email, phone=phone)
        data.save()
        messages.success(request, 'Etudiant ajouté avec succès.')

        return render(request, 'Students_templates/Students.html')
    else:
        return render(request, 'Students_templates/Students.html')
