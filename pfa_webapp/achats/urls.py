from django.urls import path

from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseUpdateView, PurchaseDeleteView

app_name = 'achats'

urlpatterns = [
    path('', PurchaseListView.as_view(), name='all'),
    path('<int:pk>/detail', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('create/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase_update'),
    path('<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase_delete'),
]
