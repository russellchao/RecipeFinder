from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Category, Choice

import json
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
            "number": 100,
            "addRecipeNutrition": "true",
            "apiKey": API_KEY,
        }

        # Dynamically handle textbox categories
        textbox_parameters = ["includeIngredients", "equipment"]
        for category_name in textbox_parameters:
            user_input = request.POST.get(category_name, "").strip()
            if user_input:
                url_params[category_name] = user_input

        # Dynamically handle checkbox categories
        checkbox_parameters = ["cuisine", "diet", "intolerances", "type"]
        for category_name, value in choice_cat.items():

            # Special Cases
            if category_name == "Meal Type": category_name = "type"

            if category_name.lower() in checkbox_parameters and value: 
                url_params[category_name.lower()] = value

        # Call the API
        response = requests.get(base_url, params=url_params)

        # Extract recipe results
        if response.status_code == 200:
            recipeResults = response.json().get("results", [])

            # print(recipeResults)

            # Write results to results.json
            # try:
            #     with open("results.json", "w") as file:
            #         json.dump(recipeResults, file, indent=4)  # Use indent=4 for pretty formatting
            #     print("Results successfully written to results.json")
            # except Exception as e:
            #     print("Error writing to results.json:", e)

            return render(request, "recipefinder/results.html", {"recipes": recipeResults})
        else:
            print("API Error:", response.status_code, response.text)
            return render(request, "recipefinder/results.html", {"recipes": []})

    return render(request, "recipefinder/results.html", {"recipes": []})






