# OCR_P10_SoftDesk

# SoftDesk

#### LITReview est site qui permet a leurs utilisateur de poster ou de demander des critiques pour des livres.

## Créer l'environnement virtuel
Placez vous dans le dossier LITReview et tapez :
`python -m venv venv`  

## Activer l'environnement virtuel

Tapez ensuite : 
`venv/scripts/activate`  

Sous Linux, ouvrez votre shell, placez vous dans le dossier LITReview et tapez : 
`source venv/bin/activate`  

### Installer les librairies nécessaire au projet

Une fois l'environnement virtuel activé, tapez :
`pip install -r requirements.txt`  

### Création d'un compte admin 
Pour créer un utilisateur admin tapez :
`python3 manage.py createsuperuser`  

Suivez les instructions, gardez en tête que lors de la saisie du mot de passe le champ reste vide mais les inputs sont bien saisis.

### Démarrer le serveur

Pour démarrer le serveur tapez :             
`python3 manage.py runserver`  

### Se rendre sur le site

Pour vous rendre sur le site, ouvrez un navigateur et dans l'url saisissez :
`127.0.0.1:8000`  
