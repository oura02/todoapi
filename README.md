# Todo API — Gestion de Tâches ✅

API REST de gestion de tâches personnelles développée avec Django
et sécurisée avec l'authentification JWT.

## Technologies
- Python 3.12 / Django 6.0
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite

## Fonctionnalités
- Inscription et connexion utilisateur
- Chaque utilisateur voit uniquement ses tâches
- CRUD complet des tâches
- Filtrage par statut et priorité
- Recherche full-text
- Tri par date et priorité
- Pagination automatique
- Token refresh automatique

## Installation
git clone https://github.com/oura02/todoapi.git
cd todoapi
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Endpoints API
- POST /api/users/register/
- POST /api/users/login/
- GET /api/users/profile/
- GET/POST /api/taches/
- GET/PUT/DELETE /api/taches/{id}/
- GET /api/taches/?statut=en_cours
- GET /api/taches/?priorite=haute
- GET /api/taches/?search=django
- GET /api/taches/mes_articles/
- POST /api/users/token/refresh/

## Statuts disponibles
- a_faire / en_cours / termine / annule

## Priorités disponibles
- basse / moyenne / haute / urgente

## Auteur
KONAN ROMEO OURA
Développeur Django Freelance — Abidjan, Côte d'Ivoire
Volontaire DjangoCon Europe 2026 — Athènes, Grèce
