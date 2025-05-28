from django import forms
from django import forms
from users.models import ProfilMedecin  # On importe depuis users.models

class ProfilMedecinForm(forms.ModelForm):
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
