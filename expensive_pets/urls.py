from django.urls import path
from .views import ExpensivePetsListView

urlpatterns = [
    path('', ExpensivePetsListView.as_view(), name='expensive_pets_list'),
]
