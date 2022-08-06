from django.shortcuts import render

# Create your views here.
from autors.models import Autor


def autors_list(request):

    return render(
        request=request,
        template_name="autor_list.html"

    )

def autor_description(request):
    autors = Autor.object.all()
    return render(
        request=request,
        template_name="autor_description.html",
        context={"autors": autors}

    )