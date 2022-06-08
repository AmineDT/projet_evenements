from django.urls import path

from . import views
from .views import ClubListView, ClubCreateView, ClubDeleteView, ClubUpdateView

app_name = 'clubs'

urlpatterns = [
    path('', ClubListView.as_view(), name='all'),
    path('<int:pk>/detail', views.ClubDetailView.as_view(), name='club_detail'),
    path('create/', ClubCreateView.as_view(), name='club_create'),
    path('<int:pk>/update/', ClubUpdateView.as_view(), name='club_update'),
    path('<int:pk>/delete/', ClubDeleteView.as_view(), name='club_delete'),
]
