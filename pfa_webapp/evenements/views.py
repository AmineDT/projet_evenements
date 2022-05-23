from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Events
import sys
from django.contrib import messages
sys.path.append("..")

# Create your views here.
from labels.models import Label

labels = Label.objects.all()


def index_evenements(request):
    if request.method == "POST":
        name_event = request.POST['name_event']
        label = Label.objects.filter(pk=request.POST.get('label', '')).first()
        date_event = request.POST['date_event']
        duration = request.POST['duration']
        budget = request.POST['budget']
        available_places = request.POST['available_places']
        data = Events(name_event=name_event, label=label, date_event=date_event, duration=duration, budget=budget,
                      available_places=available_places)
        data.save()
        messages.success(request, 'Evénement ajouté avec succès.')

        return render(request, 'Events_templates/Events.html')
    else:
        return render(request, 'Events_templates/Events.html', {'labels': labels})
