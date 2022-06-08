from django.urls import path

from .views import EventListView, EventCreateView, EventDeleteView, EventUpdateView, EventDetailView

app_name = 'evenements'

urlpatterns = [
    path('', EventListView.as_view(), name='all'),
    path('<int:pk>/detail', EventDetailView.as_view(), name='event_detail'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
]
