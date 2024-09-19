from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Media
from .forms import MediaForm

class MediaListView(ListView):
    model = Media
    template_name = 'media_list.html'

class MediaCreateView(CreateView):
    model = Media
    form_class = MediaForm
    template_name = 'media_form.html'
    success_url = '/media/'

class MediaUpdateView(UpdateView):
    model = Media
    form_class = MediaForm
    template_name = 'media_form.html'
    success_url = '/media/'

class MediaDeleteView(DeleteView):
    model = Media
    template_name = 'media_confirm_delete.html'
    success_url = '/media/'
