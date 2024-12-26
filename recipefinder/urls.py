from django.urls import path

from . import views

appname = "recipefinder"
urlpatterns = [
    path("", views.index, name="index"),
]