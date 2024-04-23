# PetRescue
## Description
PetRescue est une application web développée avec Django qui permet aux utilisateurs de signaler les animaux perdus ou trouvés dans leur région. 

## Installation
1. Clonez le dépôt GitHub :
```
git clone https://github.com/MaximeCHASLES/NR.git
```
2. Créer un environnement virtuel (optionnel) :
```
python3 -m venv .venv
```
3. Activer l'environnement virtuel:

- Sur Windows :

  ```
  .\env\Scripts\activate
  ```

- Sur macOS et Linux :

  ```
  source env/bin/activate
  ```

4. Installez les dépendances Python requises :
```
pip install -r requirements.txt
```
5. Accédez au répertoire du projet :
```
cd petrescue
```


## Utilisation
### Lancement du serveur
Pour démarrer le serveur de développement Django, exécutez la commande suivante :
```
python manage.py runserver
```
Le serveur sera accessible à l'adresse http://127.0.0.1:8000/ dans votre navigateur web.

### Effectuer les migrations
Avant de démarrer le serveur pour la première fois ou après avoir apporté des modifications aux modèles Django, vous devez effectuer les migrations pour mettre à jour la base de données. Utilisez la commande suivante :
```
python manage.py makemigrations
```
Ensuite, appliquez les migrations avec la commande :
```
python manage.py migrate
```

## Structure du Projet
```
petrescue/            # Répertoire racine du projet Django
|-- main/             # Application principale du projet
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- migrations/
|   |-- models.py
|   |-- static/
|   |   `-- main/
|   |       |-- css/
|   |       |-- img/
|   |       `-- js/
|   |-- templates/
|   |   `-- main/
|   |       |-- animaux_perdus.html
|   |       |-- animaux_trouves.html
|   |       |-- connexion.html
|   |       |-- index.html
|   |       |-- inscription.html
|   |       |-- layout/
|   |       |   |-- animaux.html
|   |       |   `-- base.html
|   |       `-- report.html
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- media/            # Répertoire pour stocker les fichiers médias (photos des animaux, etc.)
|-- petrescue/        # Configuration du projet Django
|-- manage.py         # Script de gestion du projet
|-- requirements.txt  # Fichier contenant les dépendances Python du projet
```

## Contributions
Les contributions sont les bienvenues !

## Licence
Ce projet est sous licence [...].

Enjoy