from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    return render(request, 'patients/patient_dashboard.html')

def profile_view(request):
    return render(request, 'patients/patient_profile.html')

def medical_view(request):
    return render(request, 'patients/patient_medical.html')

def alerts_view(request):
    return render(request, 'patients/patient_alerts.html')

from django.contrib.auth.decorators import login_required
from .models import PatientProfile
from .forms import PatientProfileForm

@login_required
def profile_view(request):
    profile, created = PatientProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = PatientProfileForm(instance=profile)
    return render(request, 'patients/patient_profile.html', {'form': form, 'profile': profile})