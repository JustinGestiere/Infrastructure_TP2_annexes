TP – Frontend + Backend avec Docker Compose

Dans ce tp le but est de créer une petite application composée de deux services :

- un backend qui expose une API
- un frontend qui appelle cette API et affiche la réponse

Les deux services sont lancés avec docker compose et communiquent entre eux via le réseau Docker.

Structure du projet
project/

- backend/
  - Dockerfile
  - app
- frontend/
  - Dockerfile
  - app
- docker-compose.yml

backend : API qui renvoie un message JSON
frontend : page web qui appelle l’API
docker-compose.yml : lance les deux services

Fonctionnement

Le backend expose une route :
GET /api/message

Réponse :
{
"message": "Hello from backend"
}

Le frontend appelle cette api et affiche le message dans la page web

Lancer le projet

Dans le dossier du projet :
docker compose up --build

Une fois lancé :
le frontend est accessible dans le navigateur
le frontend appelle le backend via le nom du service Docker

Tests

ouvrir le frontend dans le navigateur :

    vérifier que la page se charge
    vérifier que le message du backend s’affiche

Message du backend : Hello from backend

Docker compose permet de lancer plusieurs conteneurs et de les connecter sur un même réseau
