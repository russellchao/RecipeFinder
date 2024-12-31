from django.urls import path

from . import views

app_name = "recipefinder"
urlpatterns = [
    path("", views.index, name="index"),
    path("preferences/", views.preferences, name="preferences"),
    path("results/", views.results, name="results"),
]