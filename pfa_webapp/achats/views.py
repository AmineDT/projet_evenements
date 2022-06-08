import sys
from abc import ABC

from achats.models import Purchases
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

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
    ordering = '-purchase_date'

    def get_queryset(self):
        try:
            a = self.request.GET.get('purchases', )
        except KeyError:
            a = None
        if a:
            purchases_list = Purchases.objects.filter(
               Q(article__icontains=a)  | Q(invoice_number__icontains=a)  | Q(id_club__name_club__icontains=a)
               | Q(id_event__name_event__icontains=a)
            )
        else:
            purchases_list = Purchases.objects.all()
        return purchases_list

    class Meta:
        sortable = True


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

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner_obj = self.request.user
        obj.save
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('achats:all')


class PurchaseDetailView(PurchaseBaseView, DetailView):
    model = Purchases
    template_name = "Purchases_templates/purchase_detail.html"
    fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")

    def get_success_url(self):
        return reverse_lazy('achats:all')


class PurchaseDeleteView(PurchaseBaseView, DeleteView, ABC):
    model = Purchases
    template_name = "Purchases_templates/purchase_confirm_delete.html"
    fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")

    def get_success_url(self):
        return reverse_lazy('achats:all')

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.owner_obj == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not (self.user_passes_test(request) or self.request.user.is_superuser):
            raise PermissionDenied
        return super(PurchaseDeleteView, self).dispatch(
            request, *args, **kwargs)


class PurchaseUpdateView(PurchaseBaseView, UpdateView):
    model = Purchases
    template_name = "Purchases_templates/purchase_update.html"
    fields = ("article", "unitary_cost", "quantity", "purchase_date", "invoice_number", "id_club", "id_event")

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.owner_obj == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not (self.user_passes_test(request) or self.request.user.is_superuser):
            raise PermissionDenied
        return super(PurchaseUpdateView, self).dispatch(
            request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('achats:all')
