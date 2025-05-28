from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Patient(models.Model):
    STATUT_CHOICES = [
        ('stable', 'Stable'),
        ('surveillance', 'Surveillance'),
        ('critique', 'Critique'),
        ('urgence', 'urgence'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, blank=True)  # Ajouté dans models.py si ce n'était pas déjà

    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)

    PATHOLOGIE_CHOICES = [
    ('hypertension', 'Hypertension'),
    ('diabete', 'Diabète'),
    ('anemie', 'Anémie'),
    ('cardiopathie', 'Cardiopathie'),
    ('pneumonie', 'Pneumonie'),
    ('asthme', 'Asthme'),
    ('autre', 'Autre'),
]

    pathologie = models.CharField(max_length=50, choices=PATHOLOGIE_CHOICES, default='autre')

    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='stable')
    urgence = models.BooleanField(default=False)

    dernier_rdv = models.DateField(null=True, blank=True)
    prochain_rdv = models.DateField(null=True, blank=True)


    # Constantes vitales
    tension = models.CharField(max_length=20, blank=True)
    poids = models.CharField(max_length=20, blank=True)
    temperature = models.CharField(max_length=20, blank=True)
    frequence = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    @property
    def age(self):
        if self.date_naissance:
            today = date.today()
            return today.year - self.date_naissance.year - (
                (today.month, today.day) < (self.date_naissance.month, self.date_naissance.day)
            )
        return None
    
MOTIFS_CHOIX = [
    ('consultation', 'Consultation générale'),
    ('suivi', 'Suivi médical'),
    ('urgence', 'Urgence'),
    ('vaccination', 'Vaccination'),
    ('bilan', 'Bilan de santé'),
    ('autre', 'Autre'),
]

from django.core.exceptions import ValidationError

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(User, on_delete=models.CASCADE)
    date_rdv = models.DateField()
    heure = models.TimeField(null=True, blank=True)
    motif = models.CharField(max_length=100, choices=MOTIFS_CHOIX, default='consultation')

    
    def __str__(self):
        return f"RDV de {self.patient.nom} le {self.date_rdv}"