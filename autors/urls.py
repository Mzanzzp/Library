from django.urls import path

from autors.views import autors_list, autors_description

app_name = "autors"
urlpatterns = [
    path("", autors_list, name="autors_list"),
    path("<int:id>", autors_description, name="autors_description"),
]
