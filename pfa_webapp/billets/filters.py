import django_filters
from django.db.models import Q
from django.forms import TextInput

from .models import Tickets


class TicketsFilter(django_filters.FilterSet):
    id_event__name_event = django_filters.CharFilter(label='Nom événement', lookup_expr='icontains',
                                                     widget=TextInput(
                                                         attrs={'placeholder': 'Entrez le nom de l\'événement'}))
    name_surname = django_filters.CharFilter(label='Nom étudiant', method='name_surname_filter',
                                             widget=TextInput(
                                                 attrs={'placeholder': 'Entrez le nom de l\'étudiant'}))

    @property
    def name_surname_filter(self, queryset, name, value):
        return queryset.filter(Q(id_student__name_student__icontains=value) | Q(id_student__name_student__icontains=value))

    class Meta:
        model = Tickets
        fields = ('id_ticket', 'name_surname')
