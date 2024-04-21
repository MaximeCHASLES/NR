from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    if request.method == "POST":
        
        position = request.POST["position"]
        espece = request.POST["espece"]
        
        return render(request, "main/found.html", {
            "position": position,
            "espece": espece
        })
    return render(request, "main/found.html")


def lost(request):
    """
    Page des animaux perdus.
    Lost pets page.
    """
    return render(request, "main/lost.html")
