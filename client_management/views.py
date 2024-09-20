from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Project
from .forms import ClientForm, ProjectForm
from django.contrib.auth.decorators import login_required

# Register a new client
@login_required
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})

# List all clients
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

# Edit or delete client information
@login_required
def client_edit(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if 'save' in request.POST:
            if form.is_valid():
                form.save()
                return redirect('client_list')
        elif 'delete' in request.POST:
            client.delete()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_edit.html', {'form': form, 'client': client})

# Add a project and assign users
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

# List projects assigned to the logged-in user
@login_required
def user_projects(request):
    projects = request.user.projects.all()  # Get projects assigned to the logged-in user
    return render(request, 'user_projects.html', {'projects': projects})
@login_required
def project_list(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'project_list.html', {'projects': projects})
