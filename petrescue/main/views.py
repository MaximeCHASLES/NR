from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from main.models import Animal
from .forms import FormulaireInscription


def index(request):
    """Page d'accueil de PetRescue.

    """
    return render(request, "main/index.html")


def animaux_trouves(request):
    """Page des annonces animaux trouvés.
    
    """
    if request.method == "POST":
        position = request.POST["position"]
        espece = request.POST["espece"]
        
        
        return render(request, "main/animaux_trouves.html", {
            "position": position,
            "espece": espece
        })
    return render(request, "main/animaux_trouves.html")


def animaux_perdus(request):
    """Page des annonces des animaux perdus.
    
    """
    animaux = Animal.objects.all()

    context = {
        "animaux": animaux,
        "espece": "Animaux",
        "code": "0"
    }

    if request.method == "POST":
        position = request.POST["position"]
        espece = request.POST["espece"]
        code = request.POST["code"]
        # animaux = Animal.objects.filter()
        animaux = Animal.objects.all()

        context = {
            "position": position,
            "espece": espece,
            "animaux": animaux,
            "code": code
        }
        
        return render(request, "main/animaux_perdus.html", context)
    
    return render(request, "main/animaux_perdus.html", context)


def connexion(request):
    """Page de connexion. 
    Indispensable pour le dépôt et la gestion des annonces.
    """
    if request.method == "POST":
        identifiant = request.POST['identifiant']
        mot_de_passe = request.POST['mot_de_passe']

        utilisateur = authenticate(request, username=identifiant, password=mot_de_passe)

        if utilisateur is not None:
            login(request, utilisateur)

            context = {
                "utilisateur": utilisateur
            }

            return HttpResponseRedirect(reverse('accueil'))
        else:
            message = "Identifiant ou mot de passe incorrect"

            context = {
                "message": message
            }

            return render(request, "main/connexion.html", context)

    return render(request, "main/connexion.html")


def deconnexion(request):
    """Page de déconnexion.
    """
    logout(request)
    return HttpResponseRedirect(reverse('accueil'))


def inscription(request):
    """Page d'inscription.
    """
    if request.method == "POST":
        formulaire = FormulaireInscription(request.POST)
        if formulaire.is_valid():
            identifiant = formulaire.cleaned_data['username']
            prenom = formulaire.cleaned_data['first_name']
            nom = formulaire.cleaned_data['last_name']
            email = formulaire.cleaned_data['email']
            mot_de_passe = formulaire.cleaned_data['password1']

            utilisateur = User.objects.create_user(
                username = identifiant,
                first_name = prenom,
                last_name = nom,
                email = email,
                password = mot_de_passe
            )

            utilisateur.save()

            utilisateur = authenticate(username=identifiant, password=mot_de_passe)
            login(request, utilisateur)
            return redirect('accueil')

    formulaire_inscription = FormulaireInscription()

    context = {
        'formulaire': formulaire_inscription
    }

    return render(request, "main/inscription.html", context)



def deposer_annonce(request):
    """
    """
    return render(request, "main/report.html")