from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

# from .models import ...

# Create your views here.

def index(request):
    template = loader.get_template("recipefinder/index.html")
    context = {
        "message": "Hello!"
    }
    return HttpResponse(template.render(context, request))