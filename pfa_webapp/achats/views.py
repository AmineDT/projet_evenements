from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.core import serializers
from achats.models import Purchases
from django.contrib.auth.mixins import LoginRequiredMixin
import sys
sys.path.append("..")
from clubs.models import Clubs
from evenements.models import Events
# Create your views here.

data = serializers.serialize("python", Purchases.objects.all())



class PurchaseBaseView(View):
    class Meta:
        model = Purchases
        fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")
        success_url = reverse_lazy('achats:all')


class PurchaseListView(LoginRequiredMixin, PurchaseBaseView, ListView):
    model = Purchases
    context_object_name = 'purchases_list'
    template_name = "Purchases_templates/purchase_list.html"
    paginate_by = 10


class PurchaseCreateView(PurchaseBaseView, CreateView):
    model = Purchases
    template_name = "Purchases_templates/purchase_form.html"
    fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")

    def get_form(self):
        from django.forms.widgets import SelectDateWidget
        form = super(PurchaseCreateView, self).get_form()
        if self.request.user.is_superuser:
            form.fields['id_club'].queryset = Clubs.objects.all()
        else:
            form.fields['id_club'].queryset = Clubs.objects.filter(id_club=self.request.user.club_joined_id)
            form.fields['id_event'].queryset = Events.objects.filter(club_id=self.request.user.club_joined_id)
        form.fields['purchase_date'].widget = SelectDateWidget()
        return form

    def get_success_url(self):
        return reverse_lazy('achats:all')


class PurchaseDetailView(PurchaseBaseView, DetailView):
    model = Purchases
    template_name = "Purchases_templates/purchase_detail.html"
    fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")

    def get_success_url(self):
        return reverse_lazy('achats:all')


class PurchaseDeleteView(PurchaseBaseView, DeleteView):
    model = Purchases
    template_name = "Purchases_templates/purchase_confirm_delete.html"
    fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")

    def get_success_url(self):
        return reverse_lazy('achats:all')


class PurchaseUpdateView(PurchaseBaseView, UpdateView):
    model = Purchases
    template_name = "Purchases_templates/purchase_update.html"
    fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")

    def get_success_url(self):
        return reverse_lazy('achats:all')
