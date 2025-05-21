 
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('reporting/', views.reporting_view, name='admin_reporting'),
    path('audit/', views.audit_view, name='admin_audit'),
]
