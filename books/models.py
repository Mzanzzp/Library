from django.db import models
from autors.models import Autor


class Book(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Author: {self.author} Title: {self.title}"
