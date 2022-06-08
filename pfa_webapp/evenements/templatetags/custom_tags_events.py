import sys

from django import template

sys.path.append("..")
from billets.models import Tickets
from achats.models import Purchases

register = template.Library()

tickets = Tickets.objects.all()
purchases = Purchases.objects.all()


@register.filter(name='ticketsevents')
def get_tickets_event(self):
    return tickets.filter(id_event=self.id_event).count()


@register.filter(name='caevents')
def calculate_event(self):
    return float(tickets.filter(id_event=self.id_event).count()) * float(self.ticket_price)


@register.filter(name='purchasesevents')
def sum_purchases_event(self):
    qs = purchases.filter(id_event=self.id_event)
    result = 0
    for q in qs:
        pr = q.unitary_cost * q.quantity
        result += pr

    return result


@register.filter(name='soldeevents')
def calculate_event(self):
    qs = purchases.filter(id_event=self.id_event)
    result = 0
    for q in qs:
        pr = q.unitary_cost * q.quantity
        result += pr

    return float(tickets.filter(id_event=self.id_event).count()) * float(self.ticket_price) - \
           float(result) + float(self.budget)

