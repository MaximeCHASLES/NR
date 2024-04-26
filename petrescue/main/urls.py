from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="accueil"),
    path('utilisateur/<str:nom_utilisateur>/', views.profil_utilisateur, name='profil_utilisateur'),
    path("animaux-trouves", views.animaux_trouves, name="trouves"),
    path("animaux-perdus", views.animaux_perdus, name="perdus"),
    path("connexion", views.connexion, name="connexion"),
    path("deconnexion", views.deconnexion, name="deconnexion"),
    path("inscription", views.inscription, name="inscription"),
    path('poster-annonce', views.poster, name='poster'),
    path('poster-annonce/perdu', views.poster_perdu, name='poster_perdu'),
    

    
]

