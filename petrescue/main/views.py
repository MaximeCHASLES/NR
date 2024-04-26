from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from main.models import Animal
from .forms import Inscription, PosterPerdu

# @login_required(login_url='connexion')

def index(request):
    """Page d'accueil de PetRescue.

    """
    return render(request, "main/index.html")


def profil_utilisateur(request, nom_utilisateur):
    return render(request, "main/profil.html")


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
    if request.GET:
        ville = request.GET["ville"]
        espece = request.GET["espece"]
        code = request.GET["code"]
        animaux = Animal.objects.filter(espece__iexact=espece, ville_nom__iexact=ville, perdu=True).order_by('-date')
        nb_animaux = len(animaux)

        context = {
            "ville": ville,
            "espece": espece,
            "code": code,
            "animaux": animaux,
            "nb_animaux": nb_animaux,
            "perdu": True
        }

        return render(request, "main/animaux_perdus.html", context)
    
    else:
        animaux = Animal.objects.filter(perdu=True).order_by('-date')

        context = {
            "animaux": animaux,
            "code": "0",
            "perdu": True
        }
    
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
            return redirect(reverse('profil_utilisateur', args=[utilisateur.username]))
            # return HttpResponseRedirect(reverse('accueil'), context)
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
        formulaire = Inscription(request.POST)
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

    formulaire_inscription = Inscription()

    context = {
        'formulaire': formulaire_inscription
    }

    return render(request, "main/inscription.html", context)

def poster(request):
    return render(request, "main/poster-annonce_choix.html")


def poster_perdu(request):
    if request.method == "POST":
        formulaire = PosterPerdu(request.POST, request.FILES)
        
        if formulaire.is_valid():
            animal = formulaire.save(commit=False)
            if request.user.is_authenticated:
                animal.utilisateur = request.user
            animal.ville_nom = request.POST['ville_nom']
            animal.ville_code = request.POST['ville_code']
            animal.departement_nom = request.POST['departement_nom']
            animal.departement_code = request.POST['departement_code']
            animal.latitude = request.POST['latitude']
            animal.longitude = request.POST['longitude']
            animal.perdu = True
            animal.save()
        return HttpResponseRedirect(reverse('profil_utilisateur', args=[request.user.username]))

    else:

        formulaire = PosterPerdu()

    context = {
        "formulaire": formulaire
    }

    return render(request, "main/poster-annonce_1.html", context)





