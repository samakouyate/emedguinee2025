 
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profil_medecin
from .views import profil_medecin, modifier_profil_medecin



urlpatterns = [
    path('dashboard/', views.dashboard_view, name='medecin_dashboard'),
    path('patients/', views.list_view, name='patients_list'),
    path('patients/<int:id>/', views.detail_view, name='patient_detail'),
    path('patients/ajouter/', views.ajouter_patient, name='ajouter_patient'),
    path('patients/export/', views.export_csv, name='export_patients_csv'),
    path('patients/export-pdf/', views.export_pdf, name='export_patients_pdf'),
    path('patients/<int:patient_id>/rendez-vous/', views.prendre_rendez_vous, name='prendre_rendez_vous'),
    path('rendez-vous/<int:rdv_id>/modifier/', views.modifier_rendez_vous, name='modifier_rendez_vous'),
    path('rendez-vous/<int:rdv_id>/supprimer/', views.supprimer_rendez_vous, name='supprimer_rendez_vous'),
    path('patients/<int:patient_id>/modifier/', views.modifier_patient, name='modifier_patient'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profil/', views.profil_medecin, name='profil_medecin'),  # ✅ cette ligne est essentielle
    path('dashboard/', views.dashboard_view, name='medecins_dashboard'),
    path('profil/modifier/', views.modifier_profil_medecin, name='modifier_profil_medecin'),
    path('profil/', profil_medecin, name='profil_medecin'),
    

    

    


    
]
