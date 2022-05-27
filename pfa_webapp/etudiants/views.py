from django import forms
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.admin.widgets import AdminDateWidget
from .models import Students
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
from django.core import serializers

data = serializers.serialize("python", Students.objects.all())


class StudentBaseView(View):
    class Meta:
        model = Students
        fields = ('name_student', 'surname_student', 'study_field', 'email', 'phone')
        success_url = reverse_lazy('etudiants:all')


class StudentListView(LoginRequiredMixin, StudentBaseView, ListView):
    model = Students
    template_name = "Students_templates/student_list.html"
    paginate_by = 10
    fields = ('name_student', 'surname_student', 'study_field', 'email', 'phone')


class StudentCreateView(StudentBaseView, CreateView):
    model = Students
    template_name = "Students_templates/student_form.html"
    fields = ('name_student', 'surname_student', 'study_field', 'email', 'phone')
    def get_success_url(self):
        return reverse_lazy('etudiants:all')


class StudentDetailView(StudentBaseView, DetailView):
    model = Students
    template_name = "Students_templates/student_detail.html"
    fields = ('name_student', 'surname_student', 'study_field', 'email', 'phone')
    def get_success_url(self):
        return reverse_lazy('etudiants:all')


class StudentDeleteView(StudentBaseView, DeleteView):
    model = Students
    template_name = "Students_templates/student_confirm_delete.html"
    fields = ('name_student', 'surname_student', 'study_field', 'email', 'phone')

    def get_success_url(self):
        return reverse_lazy('etudiants:all')


class StudentUpdateView(StudentBaseView, UpdateView):
    model = Students
    template_name = "Students_templates/student_update.html"
    fields = ('name_student', 'surname_student', 'study_field', 'email', 'phone')

    def get_success_url(self):
        return reverse_lazy('etudiants:all')