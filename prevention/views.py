from django.shortcuts import render

# Create your views here.
def prevention_view(request):
    return render(request, 'prevention/prevention.html')
