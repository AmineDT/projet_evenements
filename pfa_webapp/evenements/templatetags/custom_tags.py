from django import template
import sys
sys.path.append("..")
from billets.models import Tickets
from achats.models import Purchases

register = template.Library()

tickets = Tickets.objects.all()
purchases = Purchases.objects.all()

@register.filter(name='ticketsevents')
def get_tickets_event(self):
    return len(tickets.filter(id_event=self.id_event))

@register.filter(name='caevents')
def calculate_event(self):
    return float(len(tickets.filter(id_event=self.id_event))) * float(self.ticket_price)

@register.filter(name='purchasessevents')
def sum_purchases_event(self):
    qs = purchases.filter(id_event=self.id_event)
    result = 0
    for q in qs :
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

    return float(len(tickets.filter(id_event=self.id_event))) * float(self.ticket_price) - \
           float(result) + float(self.budget)

