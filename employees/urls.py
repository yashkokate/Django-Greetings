from django.urls import path
from . import views  # Import your views from the employee app

urlpatterns = [
    path('<int:pk>/', views.employee_detail, name='employee_detail'),  # View for employee detail page
    path('add/', views.employee_add, name='employee_add'),  # View for adding a new employee with photo
    # Add other URLs as necessary
]
