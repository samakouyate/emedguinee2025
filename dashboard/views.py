from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

def reporting_view(request):
    return render(request, 'dashboard/admin_reporting.html')

def audit_view(request):
    return render(request, 'dashboard/admin_audit.html')
