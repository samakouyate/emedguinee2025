from django.db import models
from django.contrib.auth.models import User

class ProfilMedecin(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    
    specialite = models.CharField("Spécialité", max_length=100)
    numero_ordre = models.CharField("Numéro d'ordre", max_length=50)
    annees_experience = models.PositiveIntegerField("Années d'expérience")
    
    nom_cabinet = models.CharField("Nom du cabinet", max_length=150)
    adresse_cabinet = models.TextField("Adresse du cabinet")
    
    telephone = models.CharField("Téléphone du cabinet", max_length=20)
    telephone_urgence = models.CharField("Téléphone d'urgence", max_length=20, blank=True, null=True)
    fax = models.CharField("Fax", max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Profil de Dr. {self.utilisateur.last_name} ({self.specialite})"
