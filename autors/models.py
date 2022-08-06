from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.year_of_birth}"