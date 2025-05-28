from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
import csv

from patients.models import Patient, RendezVous
from patients.forms import PatientForm, RendezVousForm
from users.models import ProfilMedecin
from .forms import ProfilMedecinForm

# ✅ Vérification si c'est un médecin
def is_medecin(user):
    return user.groups.filter(name="Médecins").exists()

def only_medecins(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not is_medecin(request.user):
            messages.error(request, "⛔ Accès refusé : réservé aux médecins.")
            return redirect('profile')
        return view_func(request, *args, **kwargs)
    return wrapper

# ✅ Dashboard Médecin
@login_required
@user_passes_test(is_medecin)
def dashboard_view(request):
    patients = Patient.objects.all()
    total_patients = patients.count()
    stables = patients.filter(statut__iexact="stable").count()
    surveillances = patients.filter(statut__iexact="surveillance").count()
    urgences = patients.filter(statut__iexact="urgence").count()
    critiques = patients.filter(statut__iexact="critique").count()
    return render(request, 'medecins/medecin_dashboard.html', {
        'patients': patients,
        'total_patients': total_patients,
        'urgences': urgences,
        'surveillances': surveillances,
        'stables': stables,
        'critiques': critiques,
        'is_medecin': True,
    })

# ✅ Liste patients
@login_required
@user_passes_test(is_medecin)
def list_view(request):
    patients = Patient.objects.all()
    return render(request, 'medecins/patients_list.html', {'patients': patients})

# ✅ Détail patient
@login_required
@user_passes_test(is_medecin)
def detail_view(request, id):
    patient = get_object_or_404(Patient, pk=id)
    rendezvous = RendezVous.objects.filter(patient=patient).order_by('-date_rdv')
    return render(request, 'medecins/patient_detail.html', {
        'patient': patient,
        'rendezvous': rendezvous,
    })

# ✅ Ajouter patient
@only_medecins
def ajouter_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Patient ajouté avec succès.")
            return redirect('medecin_dashboard')
    else:
        form = PatientForm()
    return render(request, 'medecins/ajouter_patient.html', {'form': form})

# ✅ Modifier patient
@login_required
@user_passes_test(is_medecin)
def modifier_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Informations du patient mises à jour.")
            return redirect('patient_detail', id=patient.id)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'medecins/modifier_patient.html', {
        'form': form,
        'patient': patient
    })

# ✅ Prendre RDV
@login_required
@only_medecins
def prendre_rendez_vous(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rdv = form.save(commit=False)
            rdv.medecin = request.user
            rdv.patient = patient
            rdv.full_clean()
            rdv.save()
            messages.success(request, "✅ Rendez-vous enregistré.")
            return redirect('patient_detail', id=patient.id)
    else:
        form = RendezVousForm()
    return render(request, 'medecins/prendre_rendez_vous.html', {
        'form': form,
        'patient': patient
    })

# ✅ Modifier RDV
@login_required
@only_medecins
def modifier_rendez_vous(request, rdv_id):
    rdv = get_object_or_404(RendezVous, pk=rdv_id)
    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rdv)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Rendez-vous modifié.")
            return redirect('patient_detail', id=rdv.patient.id)
    else:
        form = RendezVousForm(instance=rdv)
    return render(request, 'medecins/prendre_rendez_vous.html', {
        'form': form,
        'patient': rdv.patient
    })

# ✅ Supprimer RDV
@login_required
@only_medecins
def supprimer_rendez_vous(request, rdv_id):
    rdv = get_object_or_404(RendezVous, pk=rdv_id)
    patient_id = rdv.patient.id
    rdv.delete()
    messages.success(request, "🗑️ Rendez-vous supprimé.")
    return redirect('patient_detail', id=patient_id)

# ✅ Export CSV
@only_medecins
def export_csv(request):
    query = request.GET.get('q')
    statut = request.GET.get('statut')
    patients = Patient.objects.all()
    if query:
        for mot in query.strip().split():
            patients = patients.filter(Q(nom__icontains=mot) | Q(prenom__icontains=mot))
    if statut and statut != 'tous':
        patients = patients.filter(statut__iexact=statut)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patients.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Prénom', 'Date de naissance', 'Statut'])
    for p in patients:
        writer.writerow([p.nom, p.prenom, p.date_naissance, p.statut])
    return response

# ✅ Export PDF
@only_medecins
def export_pdf(request):
    query = request.GET.get('q')
    statut = request.GET.get('statut')
    patients = Patient.objects.all()
    if query:
        for mot in query.strip().split():
            patients = patients.filter(Q(nom__icontains=mot) | Q(prenom__icontains=mot))
    if statut and statut != 'tous':
        patients = patients.filter(statut__iexact=statut)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "Liste des patients")
    p.setFont("Helvetica", 12)
    y = height - 100
    p.drawString(50, y, "Nom")
    p.drawString(150, y, "Prénom")
    p.drawString(280, y, "Date naissance")
    p.drawString(430, y, "Statut")
    y -= 25
    for pat in patients:
        p.drawString(50, y, pat.nom)
        p.drawString(150, y, pat.prenom)
        p.drawString(280, y, pat.date_naissance.strftime('%d/%m/%Y'))
        p.drawString(430, y, pat.statut.capitalize() if pat.statut else "Inconnu")
        y -= 20
        if y < 50:
            p.showPage()
            y = height - 50
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

# ✅ Afficher le profil médecin
@login_required
@user_passes_test(is_medecin)
def profil_medecin(request):
    profil = ProfilMedecin.objects.get(utilisateur=request.user)
    return render(request, 'medecins/profil_medecin.html', {'profil': profil})

# ✅ Modifier profil médecin
@login_required
@user_passes_test(is_medecin)
def modifier_profil_medecin(request):
    profil = get_object_or_404(ProfilMedecin, utilisateur=request.user)
    if request.method == 'POST':
        form = ProfilMedecinForm(request.POST, instance=profil)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Profil mis à jour.")
            return redirect('profil_medecin')
    else:
        form = ProfilMedecinForm(instance=profil)
    return render(request, 'medecins/modifier_profil_medecin.html', {'form': form})
