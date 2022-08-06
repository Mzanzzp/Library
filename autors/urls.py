from django.urls import path

from autors.views import autors_list

app_name = "autors_list"
urlpatterns = [
    path("", autors_list, name="autors_list"),
]