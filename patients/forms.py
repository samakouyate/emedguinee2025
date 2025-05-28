from django import forms
from .models import Patient


CHOIX_PATHOLOGIES = [
    ('hypertension', 'Hypertension'),
    ('diabete', 'Diabète'),
    ('anemie', 'Anémie'),
    ('cardiopathie', 'Cardiopathie'),
    ('pneumonie', 'Pneumonie'),
    ('asthme', 'Asthme'),
    ('autre', 'Autre'),
]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'dernier_rdv': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'prochain_rdv': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'urgence': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pathologie': forms.Select(attrs={'class': 'form-select'}),
        }
        
from django import forms
from .models import RendezVous

from django import forms
from .models import RendezVous
from django.core.exceptions import ValidationError

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['date_rdv', 'heure', 'motif']

    def __init__(self, *args, **kwargs):
        self.patient = kwargs.pop('patient', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date_rdv = cleaned_data.get('date_rdv')

        if self.patient and date_rdv:
            qs = RendezVous.objects.filter(patient=self.patient, date_rdv=date_rdv)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise ValidationError(f"⚠️ Ce patient a déjà un rendez-vous le {date_rdv.strftime('%d/%m/%Y')}.")

        return cleaned_data
