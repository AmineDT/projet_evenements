import sys

from django import template

sys.path.append("..")
from billets.models import Tickets
from evenements.models import Event

register = template.Library()

tickets = Tickets.objects.all()
events = Events.objects.all()


@register.filter(name='ticket price')
def get_tickets_event(self):
    return tickets.filter(id_event=self.id_event).count()


