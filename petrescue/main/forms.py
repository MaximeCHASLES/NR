from django import forms
from .models import Animal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Inscription(UserCreationForm):
    email = forms.EmailField(max_length=254)
    ville = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'first_name' , 'last_name', 'ville' , 'email', 'password1', 'password2']
        labels = {
            "username": _("Identifiant"),
            "first_name": _("Prénom")
        }


class PosterPerdu(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            # Informations générales
            "nom",
            "espece",
            "no_tatouage",
            # Description et photos
            "description",
            "photo1",
            "photo2",
            "photo3",
        ]
