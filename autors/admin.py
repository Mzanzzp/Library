from django.contrib import admin

# Register your models here.
from autors.models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass

# @admin.register(Bio)
# class BioAdmin(admin.ModelAdmin):
#     list_display = ['author', 'bio_expect']
#
#     def bio_excerpt(self, obj):
#         return f"{obj.bio[:30]} ... "