from django.db import models
from django.contrib.auth.models import User  # Use the existing User model

# Client model
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

# Project model
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
