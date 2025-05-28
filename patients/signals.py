from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import RendezVous, Patient
from datetime import date

@receiver([post_save, post_delete], sender=RendezVous)
def maj_dates_rdv_patient(sender, instance, **kwargs):
    patient = instance.patient
    tous_rdv = RendezVous.objects.filter(patient=patient)

    # Dernier RDV = le plus proche dans le passé
    derniers = tous_rdv.filter(date_rdv__lt=date.today()).order_by('-date_rdv')
    patient.dernier_rdv = derniers[0].date_rdv if derniers else None

    # Prochain RDV = le plus proche dans le futur
    prochains = tous_rdv.filter(date_rdv__gte=date.today()).order_by('date_rdv')
    patient.prochain_rdv = prochains[0].date_rdv if prochains else None

    patient.save()
