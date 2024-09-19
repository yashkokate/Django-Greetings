from django.views.generic import ListView
from .models import Pet

class ExpensivePetsListView(ListView):
    model = Pet
    template_name = 'expensive_pets_list.html'

    def get_queryset(self):
        return Pet.expensive_pets()
