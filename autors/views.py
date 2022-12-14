from django.shortcuts import render

# Create your views here.
from autors.models import Autor


def autors_list(request):
    autors = Autor.objects.all()
    return render(
        request=request,
        template_name="autor_list.html",
        context={"autors": autors},
    )

def autors_description(request, id):
    autors__ = Autor.objects.get(pk=id)
    return render(
        request=request,
        template_name="autor_description.html",
        context={"autors__": autors__},

    )