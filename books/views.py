from django.shortcuts import render

# Create your views here.
from books.models import Book


def view(request):

    books = Book.objects.all()
    return render(request=request,
                  template_name='books.html',
                  context={'books': books},
                  )


def book_details(request):
    details = Book.objects.get(pk=id)

    return render(
        request=request,
        template_name="book_details.html",
        context={'details': details}
    )
