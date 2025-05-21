 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prevention_view, name='prevention'),
]
