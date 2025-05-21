from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_view(request):
    return render(request, 'core/home.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def legal_view(request):
    return render(request, 'core/legal.html')
