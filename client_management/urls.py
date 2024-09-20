from django.urls import path
from . import views

urlpatterns = [
    path('clients/register/', views.register_client, name='register_client'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/edit/', views.client_edit, name='client_edit'),
    path('projects/add/', views.add_project, name='add_project'),
    path('my-projects/', views.user_projects, name='user_projects'),
    path('projects/', views.project_list, name='project_list')
]
