from django.urls import path

from autors.views import autors_description

app_name = "autors_descriptions"
urlpatterns = [
    path("", autors_description, name="autors_description"),
]