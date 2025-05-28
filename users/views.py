from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from users.models import ProfilMedecin


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # 🔁 Gestion du paramètre ?next=
            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)

            # 🔁 Sinon, redirection selon le rôle
            if user.is_staff:
                return redirect('/admin/')
            elif user.groups.filter(name='Médecins').exists():
                return redirect('medecin_dashboard')
            else:
                return redirect('profile')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie. Connectez-vous.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ProfilForm

@login_required
def modifier_profil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Votre profil a été mis à jour avec succès.")
            return redirect('profile')
    else:
        form = ProfilForm(instance=request.user)
    
    return render(request, 'users/edit_profile.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def redirect_after_login(request):
    user = request.user

    # Redirection selon le rôle
    if user.is_staff:
        return redirect('/admin/')
    elif user.groups.filter(name='Médecins').exists():
        return redirect('medecin_dashboard')
    else:
        return redirect('profile')
