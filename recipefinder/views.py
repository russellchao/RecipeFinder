from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Category, Choice

import requests

API_KEY = 'ef8163f9b5d64b61a449552724d38c15'

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
    if request.method == "POST":
        selected_choice_ids = request.POST.getlist("choices")

        # Reset all choices to not selected
        Choice.objects.all().update(selected=False)

        # Update only the selected choices
        Choice.objects.filter(id__in=selected_choice_ids).update(selected=True)

        # Gather the selected preferences
        selected_choices = Choice.objects.filter(selected=True)
        ingredients = ",".join([choice.choice_text for choice in selected_choices])

        # Call the Spoonacular API
        url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={API_KEY}"
        response = requests.get(url)
        recipes = response.json() if response.status_code == 200 else []

        return render(request, "recipefinder/results.html", {"recipes": recipes})

    return render(request, "recipefinder/results.html", {"recipes": []})






