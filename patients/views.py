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

