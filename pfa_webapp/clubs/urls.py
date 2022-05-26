from django.urls import path
from . import views
from .views import ClubListView


urlpatterns = [
   path('', views.index_clubs, name='index_clubs'),
   path('output/', ClubListView.as_view(), name='club_table_view'),
]