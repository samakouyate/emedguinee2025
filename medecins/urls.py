 
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='medecin_dashboard'),
    path('patients/', views.list_view, name='patients_list'),
    path('patients/<int:id>/', views.detail_view, name='patient_detail'),
]
