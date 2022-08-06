from django.shortcuts import render

# Create your views here.


def autors_list(request):

    return render(
        request=request,
        template_name="autor_list.html"

    )
