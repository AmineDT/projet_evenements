from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.core import serializers
from .models import Purchases
from django.contrib.auth.mixins import LoginRequiredMixin

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
