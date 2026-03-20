# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TacheViewSet

router = DefaultRouter()
router.register(r'taches', TacheViewSet, basename='tache')

urlpatterns = [
    path('', include(router.urls)),
]