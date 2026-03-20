# tasks/admin.py
from django.contrib import admin
from .models import Tache


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ['titre', 'proprietaire', 'statut', 'priorite', 'date_echeance']
    list_filter = ['statut', 'priorite']
    search_fields = ['titre', 'description']
    list_editable = ['statut', 'priorite']