from django.urls import path
from . import views

urlpatterns = [
    path("accueil", views.index, name="accueil"),
    path("animaux-trouves", views.animaux_trouves, name="trouves"),
    path("animaux-perdus", views.animaux_perdus, name="perdus"),
    path("connexion", views.connexion, name="connexion"),
    path("deconnexion", views.deconnexion, name="deconnexion"),
    path("inscription", views.inscription, name="inscription"),
    path("deposer-annonce", views.deposer_annonce, name="annonce")
]

