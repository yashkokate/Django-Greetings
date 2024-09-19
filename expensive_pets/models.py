from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField()  # Age in years
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price in RS

    def __str__(self):
        return self.name

    @classmethod
    def expensive_pets(cls):
        return cls.objects.filter(price__gt=5000)
