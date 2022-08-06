
from django.contrib import admin
from django.urls import path

from books.views import view, book_details

urlpatterns = [
    path('', view, name='bookview'),
    path("<int:id>", book_details, name="details"),
]
