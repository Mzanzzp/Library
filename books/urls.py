
from django.contrib import admin
from django.urls import path

from books.views import view

urlpatterns = [
    path('', view),
]
