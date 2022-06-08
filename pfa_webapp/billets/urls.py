from django.urls import path

from .views import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView

app_name = 'billets'

urlpatterns = [
    path('', TicketListView.as_view(), name='all'),
    path('<int:pk>/detail', TicketDetailView.as_view(), name='ticket_detail'),
    path('create/', TicketCreateView.as_view(), name='ticket_create'),
    path('<int:pk>/update/', TicketUpdateView.as_view(), name='ticket_update'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
]
