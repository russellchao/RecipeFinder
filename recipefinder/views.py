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


def index(request):
    return render(request, "recipefinder/index.html")
    

def preferences(request):
    Choice.objects.filter(selected=True).update(selected=False)
    categories = Category.objects.all()
    return render(request, 'recipefinder/preferences.html', {'categories': categories})


def results(request):
    if request.method == "POST":
        selected_choice_ids = request.POST.getlist("choices")
        Choice.objects.all().update(selected=False)
        Choice.objects.filter(id__in=selected_choice_ids).update(selected=True)
        selected_choices = Choice.objects.filter(selected=True)
               
        # Group choices based on category
        choice_cat = dict()
        for choice in selected_choices:
            category_name = choice.category.category_text
            if category_name not in choice_cat:
                choice_cat[category_name] = ""
            choice_cat[category_name] += choice.choice_text + ","

        # Build the API call URL
        base_url = f"https://api.spoonacular.com/recipes/complexSearch?"
        url_params = {
            "number": 15,
            "addRecipeNutrition": "true",
            "apiKey": API_KEY,
        }

        # Dynamically add categories to the API call
        allowed_parameters = ["cuisine", "diet", "intolerances", "includeIngredietns", "excludeIngredients", "type"]
        for category_name, value in choice_cat.items():
            if category_name.lower() in allowed_parameters and value: 
                url_params[category_name.lower()] = value

        # Call the API
        response = requests.get(base_url, params=url_params)
        recipes = response.json().get('results', []) if response.status_code == 200 else []

        return render(request, "recipefinder/results.html", {"recipes": recipes})

    return render(request, "recipefinder/results.html", {"recipes": []})






