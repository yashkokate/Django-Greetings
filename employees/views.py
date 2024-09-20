from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

# View to display employee details
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

# View to add a new employee
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('employee_detail', pk=form.instance.pk)
    else:
        form = EmployeeForm()

    return render(request, 'employee_add.html', {'form': form})
