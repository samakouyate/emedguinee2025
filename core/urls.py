 
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('legal/', views.legal_view, name='legal'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
]
