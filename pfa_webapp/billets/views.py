from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import sys



sys.path.append("..")
from evenements.models import Events

from billets.models import Tickets

# Create your views here.
from django.core import serializers

data = serializers.serialize("python", Tickets.objects.all())


class TicketBaseView(View):
    class Meta:
        model = Tickets
        fields = ("id_event", "id_student")
        success_url = reverse_lazy('billets:all')


class TicketListView(LoginRequiredMixin, TicketBaseView, ListView):
    model = Tickets
    template_name = "Tickets_templates/ticket_list.html"
    fields = ("id_event", "id_student")
    paginate_by = 10


class TicketCreateView(TicketBaseView, CreateView):
    model = Tickets
    template_name = "Tickets_templates/ticket_form.html"
    fields = ("id_event", "id_student")

    def get_form(self, *args, **kwargs):
        form = super(TicketCreateView, self).get_form(*args, **kwargs)
        if self.request.user.is_superuser:
            form.fields['id_event'].queryset = Events.objects.all()
        else:
            id_club = self.request.user.club_joined_id
            form.fields['id_event'].queryset = Events.objects.filter(club_id=id_club)
        return form

    def get_success_url(self):
        return reverse_lazy('billets:all')


class TicketDetailView(TicketBaseView, DetailView):
    model = Tickets
    template_name = "Tickets_templates/ticket_detail.html"
    fields = ("id_event", "id_student")

    def get_success_url(self):
        return reverse_lazy('billets:all')


class TicketDeleteView(TicketBaseView, DeleteView):
    model = Tickets
    template_name = "Tickets_templates/ticket_confirm_delete.html"
    fields = ("id_event", "id_student")

    def get_success_url(self):
        return reverse_lazy('billets:all')


class TicketUpdateView(TicketBaseView, UpdateView):
    model = Tickets
    template_name = "Tickets_templates/ticket_update.html"
    fields = ("id_event", "id_student")

    def get_success_url(self):
        return reverse_lazy('billets:all')


