from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    return render(request, 'medecins/medecin_dashboard.html')

def list_view(request):
    return render(request, 'medecins/patients_list.html')

def detail_view(request):
    return render(request, 'medecins/patient_detail.html')
