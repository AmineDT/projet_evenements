from django import forms
from django.core.checks import messages
from django.core.mail import message
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.admin.widgets import AdminDateWidget
from requests import request

from evenements.models import Events
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from django.core import serializers

import sys
sys.path.append("..")
from clubs.models import Clubs

data = serializers.serialize("python", Events.objects.all())


class EventBaseView(View):
    class Meta:
        model = Events
        fields = ('name_event', 'club', 'date_event', 'duration', 'budget', 'available_places', 'ticket_price')
        success_url = reverse_lazy('evenements:all')


class EventListView(LoginRequiredMixin, EventBaseView, ListView):
    model = Events
    template_name = "Events_templates/event_list.html"
    paginate_by = 10
    fields = ('name_event', 'club', 'date_event', 'duration', 'budget', 'available_places', 'ticket_price')




class EventCreateView(EventBaseView, CreateView):
    model = Events
    template_name = "Events_templates/event_form.html"
    fields = ('name_event', 'club', 'date_event', 'duration', 'budget', 'available_places', 'ticket_price')
    def get_form(self, *args, **kwargs):
        from django.forms.widgets import SelectDateWidget
        form = super(EventCreateView, self).get_form(*args, **kwargs)
        if self.request.user.is_superuser:
            form.fields['club'].queryset = Clubs.objects.all()
        else:
            form.fields['club'].queryset = Clubs.objects.filter(id_club=self.request.user.club_joined_id)
        form.fields['date_event'].widget = SelectDateWidget()
        return form
    def get_success_url(self):
        return reverse_lazy('evenements:all')





class EventDetailView(EventBaseView, DetailView):
    model = Events
    template_name = "Events_templates/event_detail.html"
    fields = ('name_event', 'club', 'date_event', 'duration', 'budget', 'available_places', 'ticket_price')
    def get_success_url(self):
        return reverse_lazy('evenements:all')


class EventDeleteView(EventBaseView, DeleteView):
    model = Events
    template_name = "Events_templates/event_confirm_delete.html"
    fields = ('name_event', 'club', 'date_event', 'duration', 'budget', 'available_places', 'ticket_price')

    def get_success_url(self):
        return reverse_lazy('evenements:all')


class EventUpdateView(EventBaseView, UpdateView):
    model = Events
    template_name = "Events_templates/event_update.html"
    fields = ('name_event', 'club', 'date_event', 'duration', 'budget', 'available_places', 'ticket_price')

    def get_success_url(self):
        return reverse_lazy('evenements:all')
