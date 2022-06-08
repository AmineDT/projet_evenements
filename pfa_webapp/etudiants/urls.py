from django.urls import path

from .views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView

app_name = 'etudiants'

urlpatterns = [
    path('', StudentListView.as_view(), name='all'),
    path('<int:pk>/detail', StudentDetailView.as_view(), name='student_detail'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
