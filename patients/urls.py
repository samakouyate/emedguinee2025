 
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='patient_dashboard'),
    path('profile/', views.profile_view, name='patient_profile'),
    path('medical/', views.medical_view, name='patient_medical'),
    path('alerts/', views.alerts_view, name='patient_alerts'),
]
