import sys

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

sys.path.append("..")
from evenements.models import Events
from clubs.models import Clubs
from billets.models import Tickets
from achats.models import Purchases


def index(request):
    return render(request, 'Index.html')


@login_required
def tresorerie(request):
    events = Events.objects.all()
    clubs = Clubs.objects.all()
    tickets = Tickets.objects.all()
    purchases = Purchases.objects.all()
    # ticket.ticketsEvenement.all()

    context = {
        'clubs': clubs,
        'tickets': tickets,
        'events': events,
    }

    return render(request, 'Treasury_event.html', context)


@login_required
def tresorerie_club(request):
    events = Events.objects.all()
    clubs = Clubs.objects.all()
    tickets = Tickets.objects.all()
    purchases = Purchases.objects.all()
    # ticket.ticketsEvenement.all()

    context = {
        'clubs': clubs,
        'tickets': tickets,
        'events': events,
    }

    return render(request, 'Treasury_club.html', context)
