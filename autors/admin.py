from django.contrib import admin

# Register your models here.
from autors.models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass