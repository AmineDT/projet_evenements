import django_filters

from .models import Tickets


class TicketsFilter(django_filters.FilterSet):
    id_student__name_student = django_filters.CharFilter(lookup_expr='icontains')
    id_event__name_event = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tickets
        fields = ('id_ticket',)