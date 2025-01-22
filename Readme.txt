# API de Liste de Tâches

Une API simple et efficace pour gérer les tâches (ToDo) construite avec FastAPI en Python. Ce projet démontre l'implémentation des opérations CRUD (Create, Read, Update, Delete) dans un environnement léger et évolutif.

## Fonctionnalités
- **Créer des tâches**: Ajoutez de nouvelles tâches à la liste avec des détails personnalisés.
- **Lister les tâches**: Voir toutes les tâches disponibles dans votre liste.
- **Mettre à jour les tâches**: Modifiez le statut ou les informations d'une tâche existante.
- **Supprimer les tâches**: Supprimez les tâches qui ont été complétées ou qui ne sont plus nécessaires.

## Technologies Utilisées
- **FastAPI**: Framework moderne et rapide pour la création d'APIs en Python.
- **Python**: Langage de programmation utilisé pour le développement du backend.
- **Uvicorn**: Serveur ASGI pour exécuter l'application.

## Comment Exécuter
Clonez ce dépôt:

git clone https://github.com/votre-utilisateur/votre-repository.git
Installez les dépendances nécessaires:
pip install -r requirements.txt
Démarrez le serveur:

uvicorn main:app --reload
Accédez à la documentation interactive de l'API dans le navigateur:

http://127.0.0.1:8000/docs (Swagger UI)
http://127.0.0.1:8000/redoc (Redoc)
Contribution
N'hésitez pas à ouvrir des issues ou à envoyer des pull requests pour améliorer ce projet.