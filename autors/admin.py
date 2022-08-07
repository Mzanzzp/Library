from django.contrib import admin

# Register your models here.
from autors.models import Autor, Bio


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'bio_expect']

    def bio_expect(self, obj):
        return f"{obj.bio[:30]} ... "