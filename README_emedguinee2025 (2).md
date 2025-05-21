# 🏥 Projet e_medGuinée 2025

**e_medGuinée** est une plateforme web de santé numérique développée avec Django, pensée pour améliorer l’accès, la gestion et le suivi des données médicales en Guinée. Elle s’intègre dans une vision de **gouvernance IT**, c’est-à-dire une gestion responsable, transparente, auditable et bien structurée des systèmes informatiques liés à la santé.

---

## 🎯 Objectifs du projet

- Digitaliser la relation patient-médecin-administration
- Sécuriser l’accès aux informations médicales
- Favoriser la prévention et l’éducation santé
- Mettre en place un système auditable et traçable (journal d’audit, supervision)
- Faciliter la supervision à grande échelle avec des indicateurs de performance

---

## ⚙️ Fonctionnalités principales

- Authentification sécurisée avec rôles (patient, médecin, admin)
- Dashboards adaptés à chaque profil
- Gestion complète des profils et dossiers médicaux
- Système d’alertes santé et erreurs système
- Statistiques et reporting pour les administrateurs
- Articles et modules de prévention santé
- Interface responsive basée sur Bootstrap 5
- Exportation de données (PDF/CSV)
- Respect des normes de gouvernance IT (audit, sécurité, accessibilité)

---

## 🧱 Structure complète du projet

Le projet suit une structure claire, modulaire et évolutive :

```
emedguinee2025/
├── core/         # Pages publiques (home, about, contact...)
├── users/        # Authentification, rôles, paramètres utilisateur
├── patients/     # Espace patient (profil, dossier, alertes)
├── medecins/     # Espace médecin (dashboard, patients)
├── dashboard/    # Supervision admin (statistiques, audit)
├── prevention/   # Sensibilisation santé (articles, quiz...)
├── alerts/       # Gestion des alertes système
├── templates/
│   ├── base.html
│   └── includes/
│       ├── navbar.html
│       └── footer.html
│   ├── core/
│   ├── users/
│   ├── patients/
│   ├── medecins/
│   ├── dashboard/
│   ├── prevention/
│   └── alerts/
├── static/
│   ├── css/style.css
│   └── js/script.js
└── manage.py
```

### ⚡ Commandes CMD pour recréer ce projet automatiquement :

```bat
cd C:\Users\HP
mkdir emedguinee2025
cd emedguinee2025

python -m venv env
env\Scripts\activate

pip install django
pip freeze > requirements.txt

django-admin startproject emedguinee2025 .

python manage.py startapp core
python manage.py startapp users
python manage.py startapp patients
python manage.py startapp medecins
python manage.py startapp dashboard
python manage.py startapp prevention
python manage.py startapp alerts

mkdir templates
mkdir templates\includes
mkdir static
mkdir static\css
mkdir static\js
mkdir static\images

echo. > templates\base.html
echo. > templates\includes\navbar.html
echo. > templates\includes\footer.html
echo. > static\css\style.css

echo. > core\urls.py
echo. > users\urls.py
echo. > patients\urls.py
echo. > medecins\urls.py
echo. > dashboard\urls.py
echo. > prevention\urls.py
echo. > alerts\urls.py

mkdir templates\core
echo. > templates\core\home.html
echo. > templates\core\about.html
echo. > templates\core\contact.html
echo. > templates\core\legal.html

mkdir templates\users
echo. > templates\users\login.html
echo. > templates\users\register.html
echo. > templates\users\settings.html

mkdir templates\patients
echo. > templates\patients\patient_dashboard.html
echo. > templates\patients\patient_profile.html
echo. > templates\patients\patient_medical.html
echo. > templates\patients\patient_alerts.html

mkdir templates\medecins
echo. > templates\medecins\medecin_dashboard.html
echo. > templates\medecins\patients_list.html
echo. > templates\medecins\patient_detail.html

mkdir templates\dashboard
echo. > templates\dashboard\admin_dashboard.html
echo. > templates\dashboard\admin_reporting.html
echo. > templates\dashboard\admin_audit.html

mkdir templates\prevention
echo. > templates\prevention\prevention.html

mkdir templates\alerts
echo. > templates\alerts\system_alerts.html
```

---

## 🤝 Répartition des tâches (équitable et détaillée)

### 🔵 Sama (Front + Patients + Prévention)
- Crée le socle visuel commun (`base.html`, `navbar.html`, `footer.html`)
- App `core` : pages d’accueil, à propos, contact, mentions légales
- App `patients` : dashboard, profil, alertes, données médicales
- App `prevention` : articles santé, vidéos éducatives
- Intégration Bootstrap + design responsive

### 🔴 Collaborateur (Back + Médecins + Admin + Authentification)
- App `users` : login, inscription, paramètres utilisateur
- App `medecins` : dashboard médecin, liste patients, fiche patient
- App `dashboard` : reporting, statistiques, logs d’audit
- App `alerts` : tableau d’alertes système (ex : tentative de connexion échouée)
- Sécurité, logique backend, architecture utilisateur

**🎯 Objectif : que chacun gère ses propres fichiers (urls.py, views.py, templates/)**

---

## 🧑‍💻 Règles Git & Collaboration

### Branches recommandées :
- `main` : stable
- `dev` : intégration
- `dev_sama` / `dev_collab` : branches personnelles

### Bonnes pratiques :
- Toujours `git pull` avant de coder
- Ne jamais pousser directement dans `main`
- Faire des commits clairs et utiles (`git commit -m "Ajout page profil patient"`)
- Tester localement avant de merger

---

