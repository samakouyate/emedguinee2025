


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('medecin', 'Médecin'),
        ('admin', 'Administrateur'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)