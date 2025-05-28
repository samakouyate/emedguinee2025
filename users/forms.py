from django import forms
from django.contrib.auth.models import User

from django import forms

from users.models import ProfilMedecin

class ProfilForm(forms.ModelForm):
    class Meta:
        model = ProfilMedecin
        fields = [
            'specialite',
            'numero_ordre',
            'annees_experience',
            'nom_cabinet',
            'adresse_cabinet',
            'telephone',
            'telephone_urgence',
            'fax',
        ]

