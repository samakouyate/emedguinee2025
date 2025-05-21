from django.shortcuts import render

# Create your views here.
def system_alerts_view(request):
    return render(request, 'alerts/system_alerts.html')
