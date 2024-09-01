from django.shortcuts import render
from smspool import poolapi

# Create your views here.
def landingPage(request):
    return render(request, 'index.html')
    
def dashboard(request):
    
    return render(request, 'dashboard.html', {
        'country':
    } )