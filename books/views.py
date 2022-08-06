from django.shortcuts import render

# Create your views here.


def view(request):
    return render(request=request,
                  template_name='books.html'
                  )
