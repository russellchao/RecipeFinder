from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Category, Choice

# Create your views here.

def index(request):
    return render(request, "recipefinder/index.html")
    

def preferences(request):
    # Reset the selected variable of every Choice model to False
    Choice.objects.filter(selected=True).update(selected=False)

    # Fetch all categories to display in the template
    categories = Category.objects.all()
    return render(request, 'recipefinder/preferences.html', {'categories': categories})


def results(request):
    # Change each Choice model's selected variable to True. 

    if request.method == "POST":
        # Get the list of selected choice IDs from the POST data
        selected_choice_ids = request.POST.getlist("choices")

        # Reset all choices to not selected
        Choice.objects.all().update(selected=False)

        # Update only the selected choices
        Choice.objects.filter(id__in=selected_choice_ids).update(selected=True)

    # Fetch the updated selected choices to display
    selected_choices = Choice.objects.filter(selected=True)
    return render(request, "recipefinder/results.html", {"selected_choices": selected_choices})






