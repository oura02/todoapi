# tasks/serializers.py
from rest_framework import serializers
from .models import Tache


class TacheSerializer(serializers.ModelSerializer):
    proprietaire_nom = serializers.CharField(
        source='proprietaire.username', read_only=True
    )

    class Meta:
        model = Tache
        fields = [
            'id', 'titre', 'description', 'statut', 'priorite',
            'date_echeance', 'date_creation', 'date_modification',
            'proprietaire_nom'
        ]
        read_only_fields = ['date_creation', 'date_modification', 'proprietaire_nom']


class TacheListSerializer(serializers.ModelSerializer):
    """Serializer allégé pour la liste"""
    class Meta:
        model = Tache
        fields = ['id', 'titre', 'statut', 'priorite', 'date_echeance']