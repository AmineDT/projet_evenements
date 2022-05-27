from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Clubs

# Create your views here.
from django.core import serializers
data = serializers.serialize( "python", Clubs.objects.all() )


class ClubBaseView(View):
    class Meta:
        model = Clubs
        fields = ("name_club", "description")
        success_url = reverse_lazy('clubs:all')


class ClubListView(LoginRequiredMixin, ClubBaseView, ListView):
    model = Clubs
    template_name = "Clubs_templates/club_list.html"
    fields = ("name_club", "description")
    paginate_by = 10

class ClubCreateView(ClubBaseView, CreateView):
    model = Clubs
    template_name = "Clubs_templates/club_form.html"
    fields = ("name_club", "description")
    def get_success_url(self):
        return reverse_lazy('clubs:all')

class ClubDetailView(ClubBaseView, DetailView):
    model = Clubs
    template_name = "Clubs_templates/club_detail.html"
    fields = ("name_club", "description")
    def get_success_url(self):
        return reverse_lazy('clubs:all')

class ClubDeleteView(ClubBaseView, DeleteView):
    model = Clubs
    template_name = "Clubs_templates/club_confirm_delete.html"
    fields = ("name_club", "description")
    def get_success_url(self):
        return reverse_lazy('clubs:all')


class ClubUpdateView(ClubBaseView, UpdateView):
    model = Clubs
    template_name = "Clubs_templates/club_update.html"
    fields = ("name_club", "description")
    def get_success_url(self):
        return reverse_lazy('clubs:all')