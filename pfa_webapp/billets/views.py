from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Events
import sys
from django.contrib import messages

sys.path.append("..")

# Create your views here.
from billets.models import Tickets
from etudiants.models import Students
from evenements.models import Events

events = Events.objects.all()
students = Students.objects.all()


def index_billets(request):
    if request.method == "POST":
        event = Events.objects.filter(pk=request.POST.get('event_select', '')).first()
        student = Students.objects.filter(pk=request.POST.get('student_select', '')).first()
        data = Tickets(id_event=event, id_student=student)
        data.save()
        messages.success(request, 'Billet ajouté avec succès.')

        return render(request, 'Tickets_templates/Tickets.html')
    else:
        return render(request, 'Tickets_templates/Tickets.html', {'events': events, 'students': students})
