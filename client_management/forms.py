from django import forms
from .models import Client, Project
from django.contrib.auth.models import User

# Form for creating/editing a Client
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']

# Form for creating/editing a Project
class ProjectForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Project
        fields = ['name', 'description', 'client', 'users']
