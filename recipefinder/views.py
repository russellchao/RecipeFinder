from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# from .models import ...

# Create your views here.

def index(request):
    return HttpResponse("Recipe Finder Homepage")