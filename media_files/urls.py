from django.urls import path
from .views import MediaListView, MediaCreateView, MediaUpdateView, MediaDeleteView

urlpatterns = [
    path('', MediaListView.as_view(), name='media_list'),
    path('add/', MediaCreateView.as_view(), name='media_add'),
    path('edit/<int:pk>/', MediaUpdateView.as_view(), name='media_edit'),
    path('delete/<int:pk>/', MediaDeleteView.as_view(), name='media_delete'),
]
