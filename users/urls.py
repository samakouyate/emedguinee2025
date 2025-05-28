 
from django.urls import path
from . import views
from .views import login_view, register_view, profile_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import modifier_profil
from .views import redirect_after_login


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
    ), name='password_reset_done'),
    # Étape 1 : Demande de réinitialisation
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'
    ), name='password_reset'),

    # Étape 2 : Email envoyé
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
    ), name='password_reset_done'),

    # Étape 3 : Saisie du nouveau mot de passe (via lien e-mail)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    # Étape 4 : Confirmation de succès
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('profile/edit/', modifier_profil, name='edit_profile'),
    path('redirect/', redirect_after_login, name='redirect_after_login'),

]




