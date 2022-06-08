import sys
from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2.templatetags import django_tables2 as tables
from evenements.models import Events
from django.db.models import Q

from evenements.filters import EventFilter

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilter(self.request.GET, queryset=self.get_queryset())
        return context

    class Meta:
        sortable = True





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


