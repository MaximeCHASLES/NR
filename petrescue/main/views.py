from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Page d'accueil de PetRescue.
    PetRescue's HomePage.
    """
    return render(request, "main/index.html")


def found(request):
    """
    Page des animaux trouvés.
    Found pets page.
    """
    if request.GET:
        context = {
            "location": request.GET["location"],
            "specie": request.GET["specie"]
        }
        return render(request, "main/found.html", context)

    return render(request, "main/found.html")


def lost(request):
    """
    Page des animaux perdus.
    Lost pets page.
    """
    return render(request, "main/lost.html")
