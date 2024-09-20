from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    # Image field to upload employee photo
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
