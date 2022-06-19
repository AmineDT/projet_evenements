import django_filters
from django.forms import TextInput

from .models import Events


class EventFilter(django_filters.FilterSet):
    name_event = django_filters.CharFilter(label='Nom événement', lookup_expr='icontains',
                                           widget=TextInput(attrs={'placeholder': 'Entrez le nom de l\'événement'}))
    date_event = django_filters.NumberFilter(label='Date événement', lookup_expr='month',
                                             widget=TextInput(attrs={'placeholder': 'Entrez le mois'}))

    class Meta:
        model = Events
        fields = ('club',)
