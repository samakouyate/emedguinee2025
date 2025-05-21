 
from django.urls import path
from . import views

urlpatterns = [
    path('system/', views.system_alerts_view, name='system_alerts'),
]
