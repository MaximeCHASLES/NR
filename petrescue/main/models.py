from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    nom = models.CharField(max_length=64, blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    description = models.TextField(max_length=150)
    perdu = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)
    espece = models.CharField(max_length=64)
    ville_nom = models.CharField(max_length=64, blank=True)
    ville_code = models.CharField(max_length=64, blank=True)
    departement_nom = models.CharField(max_length=64, blank=True)
    departement_code = models.CharField(max_length=5, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    photo1 = models.ImageField(upload_to="photos_animaux/")
    photo2 = models.ImageField(upload_to="photos_animaux/", blank=True)
    photo3 = models.ImageField(upload_to="photos_animaux/", blank=True)
    no_tatouage = models.CharField(max_length=16, blank=True)

    def __str__(self) -> str:
        s = ""
        if self.perdu:
            s = f"P-{self.id}-{self.departement_code}-{self.ville_code}"
        else:
            s = f"T-{self.id}-{self.departement_code}-{self.ville_code}"
        return s
    