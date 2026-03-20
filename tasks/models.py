# tasks/models.py
from django.db import models
from django.contrib.auth.models import User


class Tache(models.Model):
    PRIORITE_CHOICES = [
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
        ('urgente', 'Urgente'),
    ]

    STATUT_CHOICES = [
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name='taches')
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES,
                              default='a_faire')
    priorite = models.CharField(max_length=10, choices=PRIORITE_CHOICES,
                                default='moyenne')
    date_echeance = models.DateField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_creation']
        verbose_name = 'Tâche'
        verbose_name_plural = 'Tâches'