from django.shortcuts import render

# Create your views here.
from books.models import Book


def view(request):

    books = Book.objects.all()
    return render(request=request,
                  template_name='books.html',
                  context={'books': books},
                  )
