import sys
from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

sys.path.append("..")
from evenements.models import Events
from billets.filters import TicketsFilter
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
    ordering = ['id_ticket']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TicketsFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        try:
            search_request = self.request.GET.get('ticket', )
        except KeyError:
            search_request = None
        if search_request:
            tickets_list = Tickets.objects.filter(
                Q(id_student__name_student__icontains=search_request) | Q(id_student__surname_student__icontains=search_request) | Q(
                    id_event__name_event__icontains=search_request)
            )
        else:
            tickets_list = Tickets.objects.all()
        if self.request.user.is_superuser:
            return tickets_list.order_by('-id_ticket')
        else:
            return tickets_list.order_by('-id_ticket').filter(id_event__club=self.request.user.club_joined)


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
