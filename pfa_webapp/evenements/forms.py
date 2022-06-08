from django import forms

from projet_evenements.pfa_webapp.evenements.models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name_event', 'club', 'date_event', 'duration', 'budget', 'available_places', 'ticket_price')
        widgets = {
            'date_event': forms.DateInput(
                format=('%d-%m-%Y'), attrs={
                    'class': 'form-control',
                    'placeholder': 'Selectionnez une date',
                    'type': 'date'
                }),
        }
