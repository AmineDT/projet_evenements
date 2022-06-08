import sys

from django import template

sys.path.append("..")
from billets.models import Tickets
from achats.models import Purchases
from clubs.models import Clubs

register = template.Library()

tickets = Tickets.objects.all()
purchases = Purchases.objects.all()
clubs = Clubs.objects.all()
club1 = clubs.get(id_club=11)


@register.filter(name='caclubs')
def calculate_club(self):
    events_by_club = self.evenementsClub.all()
    result = 0
    for event_by_club in events_by_club:
        result += float(tickets.filter(id_event=event_by_club.id_event).count()) * float(event_by_club.ticket_price)
    return result


@register.filter(name='purchasesclubs')
def sum_purchases_club(self):
    events_by_club = self.evenementsClub.all()
    total_result = 0
    for event_by_club in events_by_club:
        qs = purchases.filter(id_event=event_by_club.id_event)
        for q in qs:
            pr = q.unitary_cost * q.quantity
            total_result += pr

    return total_result


@register.filter(name='budgetsclubs')
def budget_club(self):
    events_by_club = self.evenementsClub.all()
    result = 0
    for event_by_club in events_by_club:
        result += event_by_club.budget
    return float(result)


@register.filter(name='soldeclubs')
def solde_club(self):
    events_by_club = self.evenementsClub.all()
    result_billet = 0
    for event_by_club in events_by_club:
        result_billet += float(tickets.filter(id_event=event_by_club.id_event).count()) * float(
            event_by_club.ticket_price)

    result_budget = 0
    for event_by_club in events_by_club:
        result_budget += event_by_club.budget

    result_achat = 0
    for event_by_club in events_by_club:
        qs = purchases.filter(id_event=event_by_club.id_event)
        for q in qs:
            pr = q.unitary_cost * q.quantity
            result_achat += pr

    return float(result_billet) + float(result_budget) - float(result_achat)
