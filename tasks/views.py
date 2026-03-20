# tasks/views.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tache
from .serializers import TacheSerializer, TacheListSerializer


class TacheViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ['statut', 'priorite']
    search_fields = ['titre', 'description']
    ordering_fields = ['date_creation', 'date_echeance', 'priorite']
    ordering = ['-date_creation']

    def get_queryset(self):
        # Chaque utilisateur voit seulement ses propres tâches
        return Tache.objects.filter(proprietaire=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return TacheListSerializer
        return TacheSerializer

    def perform_create(self, serializer):
        # Assigner automatiquement l'utilisateur connecté
        serializer.save(proprietaire=self.request.user)