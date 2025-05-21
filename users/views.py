from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

def settings_view(request):
    return render(request, 'users/settings.html')
