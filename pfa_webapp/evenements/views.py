from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Events
import sys
from django.contrib import messages
sys.path.append("..")

# Create your views here.
from clubs.models import Club

clubs = Club.objects.all()


def index_evenements(request):
    if request.method == "POST":
        name_event = request.POST['name_event']
        club = Club.objects.filter(pk=request.POST.get('club_select', '')).first()
        date_event = request.POST['date_event']
        duration = request.POST['duration']
        budget = request.POST['budget']
        available_places = request.POST['available_places']
        ticket_price = request.POST['ticket_price']
        data = Events(name_event=name_event, club=club, date_event=date_event, duration=duration, budget=budget,
                      available_places=available_places, ticket_price=ticket_price)
        data.save()
        messages.success(request, 'Evénement ajouté avec succès.')

        return render(request, 'Events_templates/Events.html')
    else:
        return render(request, 'Events_templates/Events.html', {'clubs': clubs})
